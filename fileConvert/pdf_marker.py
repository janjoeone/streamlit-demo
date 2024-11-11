from marker.convert import convert_single_pdf
from marker.models import load_all_models

fpath = "C:/Users/yaohua.zhang/OneDrive - Accenture (China)/桌面/0eb29b4e7cbbf52827b243468a464bd6.pdf"
model_lst = load_all_models()
full_text, images, out_meta = convert_single_pdf(fpath, model_lst)
print(full_text)
print(images)
print(out_meta)