declare module './apollo' {
    import { ApolloClient } from '@apollo/client/core'
    const apolloClient: ApolloClient<any>
    export { apolloClient }
  }
  