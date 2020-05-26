
from controllers import *
from graphene_tornado.schema import Schema
from  graphene_tornado.tornado_graphql_handler import  TornadoGraphQLHandler
route = [
		(
			r"/graphql",TornadoGraphQLHandler,dict(graphiql=True,schema=Schema(query=home.Query,mutation=home.Mutations))
			
		)
]
					