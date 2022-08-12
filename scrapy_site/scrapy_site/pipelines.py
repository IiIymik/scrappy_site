from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from scrapy_site.models import Quote, Author, Tag, db_connect, create_table


class ScrapySiteSavePipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        session = self.Session()
        quote = Quote()
        author = Author()
        tag = Tag()
        author.name = item["author_name"]
        author.birthday = item["author_birthday"]
        author.bornlocation = item["author_bornlocation"]
        author.bio = item["author_bio"]
        quote.quote_content = item["quote_content"]

        exist_author = session.query(Author).filter_by(name = author.name).first()
        if exist_author is not None:
            quote.author = exist_author
        else:
            quote.author = author

        if "tags" in item:
            for tag_name in item["tags"]:
                tag = Tag(name=tag_name)
                exist_tag = session.query(Tag).filter_by(name = tag.name).first()
                if exist_tag is not None:
                    tag = exist_tag
                quote.tags.append(tag)

        try:
            session.add(quote)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item


class DuplicatesPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        exist_quote = session.query(Quote).filter_by(quote_content = item["quote_content"]).first()
        session.close()
        if exist_quote is not None:
            raise DropItem("Duplicate item found: %s" % item["quote_content"])
        else:
            return item