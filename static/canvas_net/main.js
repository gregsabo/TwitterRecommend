(function() {
  var Node, draw, initialize_canvas, initialize_nodes, nodes, x_offset, y_offset;
  x_offset = 10;
  y_offset = 10;
  nodes = [];
  Node = (function() {
    function Node(x, y) {
      this.x = x;
      this.y = y;
      this.connections = [];
    }
    Node.prototype.draw = function(ctx) {
      var connection, _i, _len, _ref, _results;
      ctx.strokeRect(this.x, this.y, 10, 10);
      _ref = this.connections;
      _results = [];
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        connection = _ref[_i];
        ctx.beginPath();
        ctx.moveTo(this.x, this.y);
        ctx.lineTo(connection.x, connection.y);
        _results.push(ctx.stroke());
      }
      return _results;
    };
    return Node;
  })();
  draw = function(ctx) {
    var node, _i, _len, _results;
    _results = [];
    for (_i = 0, _len = nodes.length; _i < _len; _i++) {
      node = nodes[_i];
      _results.push(node.draw(ctx));
    }
    return _results;
  };
  initialize_nodes = function() {
    var i, node, this_x, this_y, _i, _len, _results;
    for (i = 0; i < 10; i++) {
      this_x = Math.random() * 800;
      this_y = Math.random() * 500;
      nodes.push(new Node(this_x, this_y));
    }
    _results = [];
    for (_i = 0, _len = nodes.length; _i < _len; _i++) {
      node = nodes[_i];
      _results.push((function() {
        var _results;
        _results = [];
        for (i = 0; i <= 5; i++) {
          _results.push(node.connections.push(nodes[Math.floor(Math.random() * nodes.length)]));
        }
        return _results;
      })());
    }
    return _results;
  };
  initialize_canvas = function() {
    var canvas, ctx;
    canvas = $("canvas").get(0);
    ctx = canvas.getContext("2d");
    return setInterval(function() {
      return draw(ctx);
    }, 10);
  };
  $(function() {
    initialize_canvas();
    return initialize_nodes();
  });
}).call(this);
