HEIGHT = 500
WIDTH = 800

MAX_HOVER = 50
x_offset = 400
y_offset = 200
target_x_offset = 400
target_y_offset = 200
currentTargetNode = null
nodes = []

initialized_canvas = false

COLOR =
  background: "#FFF"
  node: "#CCC"

class Node
  constructor: (@x, @y, @name) ->
    @connections = []
    @size = 10
    @hover_x = 0
    @hover_y = 0
  
  draw: (ctx, color=COLOR.node) ->
    ctx.fillStyle = color
    ctx.strokeStyle = color
    this_x = @x + x_offset - (@size/2) + @hover_x
    this_y = @y + y_offset - (@size/2) + @hover_y
    ctx.fillRect this_x, this_y, @size, @size

    ctx.font = "bold 12px sans-serif";
    textWidth = ctx.measureText(@name);

    ctx.fillText(@name, this_x - textWidth.width/2, this_y + 30);

    for connection in @connections
      ctx.beginPath()
      ctx.moveTo(@x + x_offset + @hover_x, @y + y_offset + @hover_y)
      ctx.lineTo(connection.x + x_offset + connection.hover_x, connection.y + y_offset + connection.hover_y)
      ctx.stroke()
    @hover()
  
  hover: ->
    @hover_x += Math.random() - 0.5
    if @hover_x > MAX_HOVER
      @hover_x = MAX_HOVER
    if @hover_x < 0
      @hover_x = 0

    @hover_y += Math.random() - 0.5
    if @hover_y > MAX_HOVER
      @hover_y = MAX_HOVER
    if @hover_y < 0
      @hover_y = 0

clear_screen = (ctx) ->
  ctx.fillStyle = COLOR.background
  ctx.fillRect 0, 0, WIDTH, HEIGHT

advance_offset_target = ->
  x_offset += (target_x_offset - x_offset) * 0.05
  y_offset += (target_y_offset - y_offset) * 0.05

draw = (ctx) ->
  clear_screen(ctx)
  advance_offset_target()
  for node in nodes
    node.draw(ctx)
  if (currentTargetNode != null) 
    currentTargetNode.draw(ctx, "000")
    for node in currentTargetNode.connections
    	node.draw(ctx, "000")


  
add_node = (root_node, connections) ->
    
  RADIUS = 200  
  num_similar = connections.length
  angle = 2 * Math.PI / num_similar
  i = 0

  for connection in connections
    RADIUS = 60 * Math.random() + 140;
    this_x = Math.cos(angle * i) * RADIUS + root_node.x
    this_y = Math.sin(angle * i) * RADIUS + root_node.y
    node = new Node(this_x, this_y, connection)
    root_node.connections.push node
    nodes.push node

    i += 1

  return root_node

find_node_by_coordinates = (x, y) ->
  for node in nodes
    nx = node.x + x_offset + node.hover_x - node.size/2
    ny = node.y + y_offset + node.hover_y - node.size/2
    if nx < x and nx + node.size > x and ny < y and ny + node.size > y
        return node
  return null

bind_click_events = ->
  $('canvas').click (event) ->
    node = find_node_by_coordinates(event.offsetX, event.offsetY)

    if node
      currentTargetNode = node

      connections = getConnectionsFor(node.name, true)

      add_node(node, connections)
      target_x_offset = (-1 * node.x) + WIDTH/2
      target_y_offset = (-1 * node.y) + HEIGHT/2
      
initialize_canvas = ->
  canvas = $("canvas").get(0)
  ctx = canvas.getContext "2d"
  
  setInterval(->
    draw ctx
  , 10)


window.start_canvas_with_nodes = (initial_person, connected_names) ->
  if (!initialized_canvas)
    initialize_canvas()

  nodes = []

  this_x = 0
  this_y = 0
  root_node = new Node(this_x, this_y, initial_person)

  nodes.push(root_node)

  target_x_offset = 400
  target_y_offset = 200
 


  currentTargetNode = add_node(root_node, connected_names)
  
  if (!initialized_canvas)
    bind_click_events()

  initialized_canvas = true
    

