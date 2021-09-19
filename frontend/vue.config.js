module.exports = {
  devServer: {
    proxy: {
      "^/api": {
        target: "http://localhost:8000/api/v1/",
        changeOrigin: true,
        logLevel: "debug",
        pathRewrite: { "^/api": "" },
      },
    },
  },
};
