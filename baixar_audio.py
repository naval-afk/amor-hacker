import subprocess

# URL do vídeo
url = "https://www.youtube.com/watch?v=sVNWYFQb_Eo"

# Nome do arquivo de saída
saida = "musica_trecho.mp3"

# Tempo de início e fim do trecho
inicio = "00:01:14"
fim = "00:01:52"

# Baixar o vídeo (áudio apenas)
subprocess.run([
    "yt-dlp.exe", "-f", "bestaudio", "--extract-audio",
    "--audio-format", "mp3", "-o", "temp_audio.%(ext)s", url
])

# Cortar o trecho com ffmpeg
subprocess.run([
    "ffmpeg.exe", "-i", "temp_audio.mp3",
    "-ss", inicio, "-to", fim, "-c", "copy", saida
])

print("✅ Áudio baixado e cortado com sucesso!")
