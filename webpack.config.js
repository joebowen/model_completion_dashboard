var path = require("path")
// var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')


// module.exports = {
//   context: __dirname,
//
//   entry: './assets/js/index', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs
//
//   output: {
//       path: path.resolve('./assets/bundles/'),
//       filename: "[name]-[hash].js",
//   },
//
//   plugins: [
//     new BundleTracker({filename: './webpack-stats.json'}),
//   ],
//
//   module: {
//     loaders: [
//       { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader'}, // to transform JSX into JS
//     ],
//   },
//
//   resolve: {
//     modulesDirectories: ['node_modules', 'bower_components'],
//     extensions: ['', '.js', '.jsx']
//   },
// }

module.exports = {
  entry: [
    './assets/js/index'
  ],
  output: {
    path: path.resolve('./assets/bundles/'),
    filename: "[name]-[hash].js"
  },
  plugins: [
      new BundleTracker({filename: './webpack-stats.json'}),
    ],
  module: {
    loaders: [{
      exclude: /node_modules/,
      loader: 'babel-loader',
      query: {
        presets: ['react', 'es2015',]
      }
    },
    {
            test: /\.scss$/,
            use: [{
                loader: "style-loader" // creates style nodes from JS strings
            }, {
                loader: "css-loader" // translates CSS into CommonJS
            }, {
                loader: "sass-loader", // compiles Sass to CS
                options: {
                    includePaths: ["./node_modules/react-bootstrap-autosuggest/src"]
                }
            }]
        },

    {
      test: /\.css$/,
      loader: 'style-loader'
    }, {
  test: /\.css$/,
  loader: 'css-loader',
  query: {
  modules: true,
  localIdentName: '[name]__[local]___[hash:base64:5]'
  }
  }]
  },
  resolve: {
    extensions: ['.js', '.jsx','.css','.scss']
  }
};
