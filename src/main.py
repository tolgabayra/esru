import typer
from analyze import analyze, detect_language
from search import search
from word_distribution import word_distribution

app = typer.Typer()


@app.command(help="Metin dosyasındaki istatistik analizini gerçekleştirir.")
def analyze_command(file_path: str):
    with open(file_path, "r") as file:
        content = file.read()

    character_count, word_count, sentence_count = analyze(content)

    typer.echo(f"Karakter Sayısı: {character_count}")
    typer.echo(f"Kelime Sayısı: {word_count}")
    typer.echo(f"Cümle Sayısı: {sentence_count}")


@app.command(help="Metin dosyasında belirli bir kelimeyi arar.")
def search_command(file_path: str, keyword: str):
    with open(file_path, "r") as file:
        content = file.read()

    keyword_count = search(content, keyword)

    typer.echo(f"'{keyword}' kelimesi metin içinde {keyword_count} kez geçiyor.")


@app.command(help="Metin dosyasındaki kelime dağılımını analiz eder.")
def word_distribution_command(file_path: str):
    with open(file_path, "r") as file:
        content = file.read()

    total_words, unique_word_count = word_distribution(content)

    typer.echo(f"Toplam Kelime Sayısı: {total_words}")
    typer.echo(f"Farklı Kelime Sayısı: {unique_word_count}")
    typer.echo(
        f"Farklı Kelimelerin Yüzdesi: {unique_word_count / total_words * 100:.2f}%"
    )


@app.command(help="Metin dosyasındaki metnin dilini bulur.")
def lang_analyze_command(file_path: str):
    with open(file_path, "r") as file:
        content = file.read()

    language = detect_language(content)

    typer.echo(f"Dil: {language}")


if __name__ == "__main__":
    app()
