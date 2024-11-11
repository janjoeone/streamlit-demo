from modelscope import snapshot_download
model_dir = snapshot_download('netease-youdao/QAnything-pdf-parser')

from qanything_kernel.utils.loader import PdfLoader
# 创建 PdfLoader 类的实例
# 可以自由更改路径,filename为需要解析的pdf文件路径，save_dir_为解析后保存文件的路径
pdf_loader = PdfLoader(filename='xxx.pdf', save_dir_='/to/path/output')
# 调用 load_to_markdown 方法进行转换
markdown_directory = pdf_loader.load_to_markdown()
print(f"Markdown文件在: {markdown_directory}")