module.exports = {
  development: {
    isProduction: false,
    port: 3000,
    apiPort: 8000,
    app: {
      name: 'Django React Redux Hot Example Development'
    }
  },
  production: {
    isProduction: true,
    port: process.env.PORT || 3000,
    apiPort: process.env.API_PORT || 8000,
    app: {
      name: 'Django React Redux Hot Example Production'
    }
  }
}[process.env.NODE_ENV || 'development'];
