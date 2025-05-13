import { ApolloClient, InMemoryCache, HttpLink } from '@apollo/client/core'

const httpLink = new HttpLink({
  uri: 'http://localhost:5000/graphql'
})

export const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
})

