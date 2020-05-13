import ffmpeg
import urllib.request
import os
import time
import shutil
#download video


print('Beginning file download with urllib...')

def downloadts(url,name):
    i=0
    status =200
    #split url
    url1 = url[:url.index('media_')+6]
    url2 = url[url.index('.ts'):]
    
    while status ==200:
        try:
            filedata = urllib.request.urlopen(url1+str(i)+url2)
            time.sleep(0.005)                                 
            datatowrite = filedata.read()
            status = filedata.status
            print("downloading media section",i)
            #print(status)
            path = './'+name+'/media_'+str(i)+'.ts'
            if os.path.isdir('./'+name):
                with open(path, 'wb') as f:
                    f.write(datatowrite)
                i = i+1
            else:
                os.mkdir('./'+name)
                with open(path, 'wb') as f:
                    f.write(datatowrite)
                i = i+1

        except:
            break
            pass
    print('lastmedia is',i-1)
    return i


def buildconcat(m,name):
    con = 'concat:'
    for idx in range(m):
        con = con +'./'+name+'/media_'+str(idx)+'.ts|'
    con = con[:-1]
    print('converting and concatenating')
    return con


if __name__ == "__main__":
    url = input("请复制输入想要的视频url")
    name = input("请输入想要的视频名字")

    lastidx = downloadts(url,name)
    #lastidx = 17
    outpath = './out1/'+name+'.ts'
    if os.path.isdir('./out1'):
        ffmpeg.input(buildconcat(lastidx,name)).output('./out1/'+name+'.ts', c='copy').run()
    else:
        os.mkdir('./out1')
        ffmpeg.input(buildconcat(lastidx,name)).output('./out1/'+name+'.ts', c='copy').run()

    #remove dir
    print('cleaning up file')
    shutil.rmtree('./'+name)
