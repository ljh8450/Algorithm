def solution(genres, plays):
    answer = []
    songs = {}
    genres_set = list(set(genres))
    length = len(plays)
    total_list = []
    for genre in genres_set: # 딕셔너리에 장르별 공간 마련
        if songs.get(genre) == None:
            songs[genre] = list()
    for i in range(length): # 딕셔너리에 값 들어가게 하기
        genre, play = genres[i], plays[i]
        songs[genre].append((play, i))
    for genre in genres_set: # 정렬 조건을 위한 총 재생 수 담기
        total = 0
        for play, index in songs[genre]:
            total += play
        total_list.append((genre, total))
    total_list.sort(key=lambda x: x[1], reverse=True) # 총 재생 수 기준 정렬
    for genre in genres_set:
        songs[genre].sort(key=lambda x:(-x[0], x[1]))
    genre_length = len(genres_set)

    for i in range(genre_length):
        genre = total_list[i][0]
        for play, idx in songs[genre][:2]:
            answer.append(idx)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))