import datetime
from statistics import mean
ha=[]
ma=[]
sa=[]
day=[]
def parse_duration(a):
      print(a)
      d=str(a).find('D')
      if(d>-1):
        day_start=str(a).find('P')+1
        day_end=d
        day=a[day_start:day_end]
        hr_start = str(a).find('T')+1
        hr_end = str(a).find('H')
        if(hr_end>-1):
            hr=a[hr_start:hr_end]
            ha.append(hr)
            min_start=hr_end+1
            min_end=str(a).find('M')
            if(min_end>-1):
                m=a[min_start:min_end]
                ma.append(m)
                sec_start=min_end+1
                sec_end=str(a).find('S')
                if sec_end >-1 :
                    s=a[sec_start:sec_end]
                    sa.append(s)
        else:
                min_start=hr_start
                min_end=str(a).find('M')
                if(min_end>-1):
                    m=a[min_start:min_end]
                    ma.append(m)
                    sec_start=min_end+1
                    sec_end=str(a).find('S')
                    if sec_end >-1:
                        s=a[sec_start:sec_end]
                        sa.append(s)
                    else:
                        sec_start=min_start
                        sec_end=str(a).find('S')
                        if sec_end >-1 :
                            s=a[sec_start:sec_end]
                            sa.append(s)

      else:

        hr_start = str(a).find('P')+2
        hr_end = str(a).find('H')
        if(hr_end>-1):
            hr=a[hr_start:hr_end]
            ha.append(hr)
            min_start=hr_end+1
            min_end=str(a).find('M')
            if(min_end>-1):
                m=a[min_start:min_end]
                ma.append(m)
                sec_start=min_end+1
                sec_end=str(a).find('S')
                if sec_end >-1 :
                    s=a[sec_start:sec_end]
                    sa.append(s)
        else:
                min_start=hr_start
                min_end=str(a).find('M')
                if(min_end>-1):
                    m=a[min_start:min_end]
                    ma.append(m)
                    sec_start=min_end+1
                    sec_end=str(a).find('S')
                    if sec_end >-1:
                        s=a[sec_start:sec_end]
                        sa.append(s)
                    else:
                        sec_start=min_start
                        sec_end=str(a).find('S')
                        if sec_end >-1 :
                            s=a[sec_start:sec_end]
                            sa.append(s)
        
      return 



def avg_duration(video_df):

    global ha
    global ma
    global sa
    global day

    ha=[]
    ma=[]
    sa=[]
    day=[]
    
    video_df['video_duration'].apply(parse_duration)
    days=sum(map(int,''.join(day)))
    hrs=sum(map(int,''.join(ha)))
    mins=sum(map(int,''.join(ma)))
    secs=sum(map(int,''.join(sa)))
    print(days,hrs,mins,secs)
    
    day_sec=(days*24)*60*60
    hrs_sec= hrs*60*60
    tsec=(mins)*60
    t_secs=secs+(tsec)+hrs_sec+day_sec
    total_len=len(day)+len(ha)+len(ma)+len(sa)
    avg_sec=t_secs/total_len
    return avg_sec











