import matplotlib.pyplot as plt
import wordcloud
from framework.Utilities.Misc.Utils import path_join


class blWordCloud:
    @staticmethod
    def generate_word_cloud():
        print("Generating word clouds...")
        vape_word_tags_path = path_join("resources", "storage", "WordTagsVape.xls")
        tobacco_word_tags_path = path_join(
            "resources", "storage", "WordTagsTobacco.xls"
        )

        vape_words = blWordCloud.read_file(vape_word_tags_path)
        tobacco_words = blWordCloud.read_file(tobacco_word_tags_path)

        wordcloud_vape = wordcloud.WordCloud(
            width=500,
            height=500,
            background_color="white",
            stopwords=set(wordcloud.STOPWORDS),
            min_font_size=10,
        ).generate(vape_words)

        wordcloud_tobacco = wordcloud.WordCloud(
            width=500,
            height=500,
            background_color="white",
            stopwords=set(wordcloud.STOPWORDS),
            min_font_size=10,
        ).generate(tobacco_words)

        figure = plt.figure()

        figure.add_subplot(1, 2, 1)
        plt.title("Vape Word Cloud")
        plt.imshow(wordcloud_vape)

        # disable ticks
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)

        figure.add_subplot(1, 2, 2)
        plt.title("Tobacco Word Cloud")
        plt.imshow(wordcloud_tobacco)

        # disable ticks
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)

        plt.show()
        return

        pass

    @staticmethod
    def read_file(path):
        import xlrd

        workbook = xlrd.open_workbook(path)
        sheet = workbook.sheet_by_index(0)
        data = []

        for counter in range(1, sheet.nrows):
            row_values = sheet.row_values(counter)
            data.append(row_values[0])

        return " ".join(data)
