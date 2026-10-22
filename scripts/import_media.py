import urllib.request, pathlib, hashlib
assets = {'assets/carnival-map-preview.webp': '8763fbbcdfa9958336bbc7046f6143905acad6c305cd45b0b2ee85b536a688f1', 'assets/carnival-map.png': '80bfad9572b98dde0ff5e3e6fc8f0bad077156b942e8abeb5e04d50e5fe37ac9', 'assets/carnival-song.mp3': '4a35e4032ffd4882a3185b23be53b43f09ec2c6567d68298b6aa95c66be05085', 'assets/carnival-ticket.webp': '91723627da0e29ae6e2fc7e95805af410821ab0b440aa57a8699826a45d5fac4', 'assets/opening-narration.mp3': '25e4f7ed59c2443ab12646e73f5e8500964587712b9f53d8325f6407df0dc492'}
base = 'https://twilight-at-the-ticket-booth.earthy-melon-3198.chatgpt.site/'
for name, expected in assets.items():
    data = urllib.request.urlopen(base+name).read()
    assert hashlib.sha256(data).hexdigest() == expected, name
    target = pathlib.Path(name)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
