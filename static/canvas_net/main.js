(function() {
  var COLOR, HEIGHT, MAX_HOVER, Node, WIDTH, add_node, advance_offset_target, bind_click_events, clear_screen, draw, find_node_by_coordinates, initialize_canvas, nodes, target_x_offset, target_y_offset, x_offset, y_offset;
  HEIGHT = 500;
  WIDTH = 800;
  MAX_HOVER = 50;
  x_offset = 400;
  y_offset = 200;
  target_x_offset = 400;
  target_y_offset = 200;
  nodes = [];
  COLOR = {
    background: "#FFF",
    node: "#000"
  };
  Node = (function() {
    function Node(x, y) {
      this.x = x;
      this.y = y;
      this.connections = [];
      this.size = 10;
      this.hover_x = 0;
      this.hover_y = 0;
    }
    Node.prototype.draw = function(ctx) {
      var connection, this_x, this_y, _i, _len, _ref;
      ctx.fillStyle = COLOR.node;
      this_x = this.x + x_offset - (this.size / 2) + this.hover_x;
      this_y = this.y + y_offset - (this.size / 2) + this.hover_y;
      ctx.fillRect(this_x, this_y, this.size, this.size);
      _ref = this.connections;
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        connection = _ref[_i];
        ctx.beginPath();
        ctx.moveTo(this.x + x_offset + this.hover_x, this.y + y_offset + this.hover_y);
        ctx.lineTo(connection.x + x_offset + connection.hover_x, connection.y + y_offset + connection.hover_y);
        ctx.stroke();
      }
      return this.hover();
    };
    Node.prototype.hover = function() {
      this.hover_x += Math.random() - 0.5;
      if (this.hover_x > MAX_HOVER) {
        this.hover_x = MAX_HOVER;
      }
      if (this.hover_x < 0) {
        this.hover_x = 0;
      }
      this.hover_y += Math.random() - 0.5;
      if (this.hover_y > MAX_HOVER) {
        this.hover_y = MAX_HOVER;
      }
      if (this.hover_y < 0) {
        return this.hover_y = 0;
      }
    };
    return Node;
  })();
  clear_screen = function(ctx) {
    ctx.fillStyle = COLOR.background;
    return ctx.fillRect(0, 0, WIDTH, HEIGHT);
  };
  advance_offset_target = function() {
    x_offset += (target_x_offset - x_offset) * 0.05;
    return y_offset += (target_y_offset - y_offset) * 0.05;
  };
  draw = function(ctx) {
    var node, _i, _len, _results;
    clear_screen(ctx);
    advance_offset_target();
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
      nx = node.x + x_offset + node.hover_x - node.size / 2;
      ny = node.y + y_offset + node.hover_y - node.size / 2;
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
      if (node) {
        add_node(node);
        target_x_offset = (-1 * node.x) + WIDTH / 2;
        return target_y_offset = (-1 * node.y) + HEIGHT / 2;
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
