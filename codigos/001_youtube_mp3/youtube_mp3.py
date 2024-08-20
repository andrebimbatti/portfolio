from yt_dlp import YoutubeDL
import os

os.system('cls')

def download_youtube_em_mp3(url, caminho_saida=''):
    caminho_saida = r"D:\Meus Documentos\Músicas" #Atualizar o caminho para a pasta que deseja que salve o mp3
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{caminho_saida}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# URL do vídeo do YouTube
video_url = input('Cole o link do Youtube que deseja baixar aqui: ')

# Baixa o vídeo como .mp3
download_youtube_em_mp3(video_url)
