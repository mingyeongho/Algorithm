from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(list)
    play_dic = defaultdict(int)
    for i in range(len(genres)):
        dic[genres[i]].append((plays[i], i))
        play_dic[genres[i]] += plays[i]
    
    sorted_genres = sorted(play_dic.keys(), key=lambda x: play_dic[x], reverse=True)
    answer = []
    
    for genre in sorted_genres:
        dic[genre].sort(key=lambda x: (-x[0], x[1]))
        for _, idx in dic[genre][:2]:
            answer.append(idx)
    
    return answer
            