from pathlib import Path


class Base():

    """
    创建图片和材质文件夹
    获取图片和材质
    """

    def __init__(self):

        self.path = Path('.')
        self.skl_dir_path = self.path / "Skills"
        self.pic_dir_path = self.path / "Pictures"
        self.tex_dir_path = self.path / "Textures"

        self.skl_dir_path.mkdir(exist_ok=True)
        self.pic_dir_path.mkdir(exist_ok=True)
        self.tex_dir_path.mkdir(exist_ok=True)


    def get_pic_paths(self):

        self.pic_paths = []
        for suffix in ["jpg", "png", "gif"]:
            for path in self.pic_dir_path.glob("*." + suffix):
                self.pic_paths.append(path)
        return len(self.pic_paths)


    def get_tex_paths(self):

        # 这俩后缀长度不一样让蠢驴非常难受

        png_paths = [path for path in self.tex_dir_path.glob("*.png")]
        json_paths = [path for path in self.tex_dir_path.glob("*.json")]

        png_stems = [path.stem for path in png_paths]
        if png_stems != [path.stem for path in json_paths]:
            return False

        self.tex_paths = []
        for i in range(len(png_stems)):
            self.tex_paths.append({png_stems[i]: (json_paths[i], png_paths[i])})
        return len(png_stems)


    def write_skill(self, name, content):

        with open(self.skl_dir_path / (name + ".yml"), "w", encoding="utf-8") as yml:
            yml.write(content)
