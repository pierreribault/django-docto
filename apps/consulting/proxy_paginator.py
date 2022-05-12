


from asyncio.log import logger


class ProxyPaginator(object):
    """
    A proxy object for returning Elasticsearch results that is able to be
    passed to a Paginator.
    """

    def __init__(self, es, index=None, body=None):
        self.es = es
        self.index = index
        self.body = body

    def __len__(self):
        return self

    def __getitem__(self, item):
        return [
            {
                'id': 1,
                'name': 'test'
            }
        ]