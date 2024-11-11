url = 'https://v2.kwaicdn.com/ksc2/2VRec4qaMwtVqho7DnK6GW4AK2z4HsMnuJ-JQmP1k8Hi7lV4eR29LgdXDu6ZnpP-MdyDuOyL5JjuFF70hjnxiP9KxsHJhDyALfhKkiH4J2OsnycimD7yW1609d-jxhGe.mp4?pkey=AAXy_TuvMlsF9adNnh1Mz9HNFSwTyenPhjNM3f5XUIpBd45eN3TOpaC-Ut6mGkyfeAoanVF08Rogajq8PayEKRmxn_b6VNqnyYpXeuefoPfqte2TLdy6deXDw6IxLC2T9IM&tag=1-1729859406-unknown-0-k4qnqbgds4-1b62c9bf2d721f37&clientCacheKey=3x3gzbc4rd5ws42_a707a0ad&di=7771b996&bp=14944&tt=hd15&ss=vp'

import requests

response = requests.get(url)
print(response.status_code)
print(response.content)
f = open('C:/Users/yaohua.zhang/OneDrive - Accenture (China)/桌面/kuaishou.mp4', 'wb').write(response.content)