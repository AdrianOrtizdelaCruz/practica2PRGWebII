from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS
import graphene

# Base de datos en memoria
productos_data = [
    {"id": 1, "nombre": "Camiseta", "precio": 19.99, "stock": 5, "disponible": True},
    {"id": 2, "nombre": "Pantalón", "precio": 39.99, "stock": 0, "disponible": False},
    {"id": 3, "nombre": "Zapatos", "precio": 59.99, "stock": 2, "disponible": True}
]

class Producto(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()
    disponible = graphene.Boolean()

class Query(graphene.ObjectType):
    productos = graphene.List(Producto)

    def resolve_productos(root, info):
        return productos_data

class ModificarStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        cantidad = graphene.Int(required=True)

    producto = graphene.Field(Producto)

    def mutate(self, info, id, cantidad):
        for prod in productos_data:
            if prod["id"] == id:
                prod["stock"] += cantidad
                if prod["stock"] <= 0:
                    prod["stock"] = 0
                    prod["disponible"] = False
                else:
                    prod["disponible"] = True
                return ModificarStock(producto=prod)
        raise Exception("Producto no encontrado")

class Mutation(graphene.ObjectType):
    modificar_stock = ModificarStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
CORS(app)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(debug=True)
