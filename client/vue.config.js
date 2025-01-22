const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  pluginOptions: {
    quasar: {
      importStrategy: 'kebab',
      rtlSupport: false
    }
  },
  transpileDependencies: [
    'quasar'
  ],

  devServer: {
    proxy: {
      "/api": {
        target: `http://127.0.0.1:8000`,
        changeOrigin: true,
        logLevel: "debug",
        ws: true,
        secure: false,
        pathRewrite: {
            '^/api': ''
        },
        headers: {
          Connection: "keep-alive",
        },
      },
    },
  },

})
