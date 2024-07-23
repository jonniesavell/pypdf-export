from pypdf import PdfReader
import stanza

upos = ['ADJ', 'ADV', 'ADP', 'VERB', 'PROPN', 'NOUN']
en_nlp = stanza.Pipeline('en', download_method=DownloadMethod.REUSE_RESOURCES)
reader = PdfReader('./data/true-pdf-sample.pdf')

try:
    for page in reader.pages:
        text_body = page.extract_text()
        en_doc = en_nlp(text_body)

        for sentence in en_doc.sentences:
            for word in sentence.words:
                if word.upos in upos:
                    print(word.lemma)
finally:
    reader.close()
