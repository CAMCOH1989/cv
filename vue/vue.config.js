const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  configureWebpack: {
    plugins: [
      // new BundleAnalyzerPlugin(),
    ],
  },
  devServer: {
    host: 'cv.local',
    port: 8286,
    allowedHosts: ['cv.local'],
  },
};
