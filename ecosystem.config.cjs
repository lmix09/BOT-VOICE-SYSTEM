module.exports = {
  apps: [
    {
      name: 'stay-voice-bot',
      script: 'src/index.js',
      env: {
        NODE_ENV: 'production',
      },
    },
  ],
}