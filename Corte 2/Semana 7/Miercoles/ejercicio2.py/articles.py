class Articulo:
  def __init__(self, title, summary,body, n_images, creation_date, writer ):
    self.title=title
    self.summary=summary
    self.body=body
    self.n_images=n_images
    self.creation_date=creation_date
    self.writer=writer


class Approved(Articulo):
  def __init__(self, title, summary, body, n_images, creation_date, writer, publication_date, approved_by):
    Articulo.__init__(self, title, summary, body, n_images, creation_date, writer)
    self.publication_date=publication_date
    self.approved_by=approved_by


  