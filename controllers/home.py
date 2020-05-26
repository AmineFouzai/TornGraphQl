
'''
Preset controller by torn for / route
'''
from .modules import *

class Post(graphene.ObjectType):
	_id=graphene.ID()
	title=graphene.String()
	body=graphene.String()

class Query(graphene.ObjectType):
	posts=graphene.List(Post)

	def resolve_posts(self,info):
		data=session.query(Posts)
		posts= [ Post(_id=res.id,title=res.title,body=res.body) for res in data]
		return posts


class  CreatePost(graphene.Mutation):
	class Arguments:
		title=graphene.String()
		body=graphene.String()
	posts=graphene.List(Post)		
	def mutate(self,info,title,body):
		session.add(Posts(title=title,body=body))
		session.commit()
		data=session.query(Posts)
		posts=[ Post(_id=res.id,title=res.title,body=res.body) for res in data]
		return CreatePost(posts)

#46
class DeletePost(graphene.Mutation):
	class Arguments:
		_id=graphene.ID()
	posts=graphene.List(Post)
	def  mutate(self,info,_id):
		p=session.query(Posts).filter(Posts.id==_id).one()
		session.delete(p)
		session.commit()
		data=session.query(Posts)
		posts=[ Post(_id=res.id,title=res.title,body=res.body) for res in data]
		return DeletePost(posts)

class UpdatePost(graphene.Mutation):
	class Arguments:
		_id=graphene.ID()
		title=graphene.String()
		body=graphene.String()
	posts=graphene.List(Post)
	def mutate(self,info,_id,title,body):
		session.query(Posts).filter(Posts.id==_id).update({
			"title":title,
			"body":body
		})
		session.commit()
		data=session.query(Posts)
		posts=[Post(_id=res.id,title=res.title,body=res.body) for res in data]	
		return 	UpdatePost(posts)
		



class Mutations(graphene.ObjectType):
	create_post=CreatePost.Field()
	delete_post=DeletePost.Field()
	update_post=UpdatePost.Field()


