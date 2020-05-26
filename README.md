# TornGraphQl
A Simple Python GraphQL API Built with Tornado and SQLalchemy for managing crud life cycle of a Post object.
# #setup:

<table>
<tr>
<td> 1)  git clone https://github.com/MedAmineFouzai/TornGraphQl</td>
</tr>
<tr>
<td> 2) cd TornGraphQl</td>
</tr>
<tr>
<td> 3) pip install pipenv</td>
</tr>
</tr>
<td> 4) pipenv --python 3.6</td>
</tr>
<tr>
<td> 5) pipenv install - r requirements.txt</td>
</tr>
<tr>
  <td>
    6) run project with <a href="https://pypi.org/project/torn/">torn cli</a> : <b>#command: [ torn run ] </b>  </td>
 </tr>
</table>

------------------------------------

## GraphQL

<img src="https://graphql.org/img/logo.svg" width="200">

[GraphQL](https://graphql.org/) is a query language for your API, and a server-side runtime for executing queries by using a type system you define for your data. GraphQL isn't tied to any specific database or storage engine and is instead backed by your existing code and data.
## Graphene-Python
<img src="https://habrastorage.org/getpro/habr/post_images/458/645/f18/458645f180f8fff23bcbd543065d8c11.png" >

[graphene-tornado](https://github.com/graphql-python/graphene-tornado) A project for running Graphene on top of Tornado for Python 3. The codebase was originally a port of graphene-django.

[Graphene-Python](https://graphene-python.org/) is a library for building GraphQL APIs in Python easily, its main goal is to provide a simple but extendable API for making developers' lives easier.

------------------------------------------

# #Usage:

Playground: http://localhost:8000/graphql 

now you can send requests via querys and see the result " YOUR API IS A USER INTERFACE !"

## querys
Get Posts:

     {
       posts {
           Id
           title
           body
       }
     }

Create Posts:
        
        mutation{
            createPost(title:"post n ",body:"this is post n"){
                posts {
                    Id
                    title
                    body
                 }
              } 
           }

Delete Posts:

      mutation{
          deletePost(Id:"xxxxx"){
              posts {
                  Id
                  title
                  body
              }
           }
        }

Update Posts:

      mutation{
          updatePost(Id:"xxxxx",title:"post n ",body:"this post n"){
              posts {
                  Id
                  title
                  body
               }
            }
          }



