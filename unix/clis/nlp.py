import spacy
import click

nlp = spacy.load("en_core_web_sm")


@click.command()
def run():
    with click.get_text_stream("stdin") as stdin:
        while stdin.readable():
            line = stdin.readline()
            if line:
                # Copy paste
                doc = nlp(line.strip())
                for ent in doc.ents:
                    print(ent.text, ent.label_)


if __name__ == "__main__":
    run()
