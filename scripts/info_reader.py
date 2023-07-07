import json


def read_metadata(path, metadata):
    """Reads the JSON metadata from a .info file"""
    text_path = str(path)
    with open(text_path.replace(".safetensors", ".civitai.info"), mode="r", encoding="utf8") as file:
        info = json.load(file)
        rewrite_if_no_value(info, "name", metadata, "ssmd_display_name")
        rewrite_if_no_value(info, "trainedWords", metadata, "ssmd_keywords")


def rewrite_if_no_value(src, src_key, dst, dst_key):
    if src is None:
        if not hasattr(src, src_key):
            return
    if dst is None:
        return
    dst[dst_key] = src[src_key]
