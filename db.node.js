const jsonServer  = require('json-server');
const server      = jsonServer.create();
const router      = jsonServer.router('x');        // Ania Kubow is passing in here db file hear but i do something different read the damn boooks.
const middlewares = jsonServer.defaults();
const port        = process.env.PORT || 3000;
         server.use(middlewares);
         server.use(router);
         server.listen(port);
