import xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin,base64
pipcan = base64.b64decode
PLUGIN=pipcan('cGx1Z2luLnZpZGVvLmpkdHY=')
reason = xbmcaddon.Addon(id=PLUGIN)
lighter = reason.getSetting(pipcan('cGFzc3dvcmQ='))
singer = reason.getSetting(pipcan('dXNlcm5hbWU='))
active = reason.getSetting(pipcan('YWN0aXZl'))
view = reason.getSetting(pipcan('dmlldw=='))
dialog = xbmcgui.Dialog()
def noguide():
    r = requests.get('http://reboothost.net:8080/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=0'%(singer,lighter))
    match = re.compile('<title>(.+?)</title><description/><desc_image><!\[CDATA\[(.+?)]]></desc_image><category_id>0</category_id><stream_url><!\[CDATA\[(.+?)]').findall(r.content)
    for  name,icon,url in match:
        grays(pipcan(name).replace('\/','/'),url.replace('.ts','.m3u8'),3,icon.replace('\/','/'),'','')
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
def hello(url):
        try:
            play=xbmc.Player()
            play.play(url)  
        except:
            pass 
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]  
        return param
def grays(pillow,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&pillow="+urllib.quote_plus(pillow)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(pillow, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": pillow, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok            
params=get_params()
url=None
pillow=None
mode=None
iconimage=None
fanart=None
description=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        pillow=urllib.unquote_plus(params["pillow"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "pillow: "+str(pillow)
if mode==None or url==None or len(url)<1:
        print ""
        noguide()
elif mode==3:
        hello(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))