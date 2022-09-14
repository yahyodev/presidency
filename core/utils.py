from django.utils.text import slugify


def unique_slug_generator(model, self):
    obj = model.objects.filter(id=self.id).first()
    if obj and obj.slug == self.slug:
        return self.slug
    origin_slug = slugify(str(self.slug))
    unique_slug = origin_slug
    numb = ''
    while g := model.objects.filter(slug=unique_slug).first():
        if g.id == self.id:
            self.slug = unique_slug
            return self.slug
        unique_slug = '%s%s%s' % (origin_slug, numb and '-', numb)
        numb = (numb or 0) + 1
    self.slug = unique_slug
    return self.slug
