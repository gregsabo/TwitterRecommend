(function() {
  var Node, add_node, bind_click_events, draw, find_node_by_coordinates, initialize_canvas, nodes, x_offset, y_offset;
  x_offset = 400;
  y_offset = 200;
  nodes = [];
  Node = (function() {
    function Node(x, y) {
      this.x = x;
      this.y = y;
      this.connections = [];
      this.size = 10;
    }
    Node.prototype.draw = function(ctx) {
      var connection, _i, _len, _ref, _results;
      ctx.strokeRect(this.x + x_offset - (this.size / 2), this.y + y_offset - (this.size / 2), this.size, this.size);
      _ref = this.connections;
      _results = [];
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        connection = _ref[_i];
        ctx.beginPath();
        ctx.moveTo(this.x + x_offset, this.y + y_offset);
        ctx.lineTo(connection.x + x_offset, connection.y + y_offset);
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
  add_node = function(root_node) {
    var RADIUS, angle, i, node, num_similar, this_x, this_y, _results;
    if (!root_node) {
      this_x = 0;
      this_y = 0;
      root_node = new Node(this_x, this_y);
      nodes.push(root_node);
    }
    RADIUS = 200;
    num_similar = Math.floor(Math.random() * 20);
    angle = 2 * Math.PI / num_similar;
    _results = [];
    for (i = 0; (0 <= num_similar ? i < num_similar : i > num_similar); (0 <= num_similar ? i += 1 : i -= 1)) {
      this_x = Math.cos(angle * i) * RADIUS + root_node.x;
      this_y = Math.sin(angle * i) * RADIUS + root_node.y;
      node = new Node(this_x, this_y);
      root_node.connections.push(node);
      _results.push(nodes.push(node));
    }
    return _results;
  };
  find_node_by_coordinates = function(x, y) {
    var node, nx, ny, _i, _len;
    for (_i = 0, _len = nodes.length; _i < _len; _i++) {
      node = nodes[_i];
      nx = node.x + x_offset;
      ny = node.y + y_offset;
      if (nx < x && nx + node.size > x && ny < y && ny + node.size > y) {
        return node;
      }
    }
    return null;
  };
  bind_click_events = function() {
    return $('canvas').click(function(event) {
      var node;
      node = find_node_by_coordinates(event.offsetX, event.offsetY);
      console.log(node);
      if (node) {
        return add_node(node);
      }
    });
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
    add_node();
    return bind_click_events();
  });
}).call(this);
