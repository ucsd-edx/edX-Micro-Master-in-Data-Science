{%- extends 'basic.tpl' -%}
{% from 'mathjax.tpl' import mathjax %}

{%- block any_cell scoped -%}
{%- if cell.metadata.get('slide_start', False) -%}
<section>
{%- endif -%}
{%- if cell.metadata.get('subslide_start', False) -%}
<section>
{%- endif -%}
{%- if cell.metadata.get('fragment_start', False) -%}
<div class="fragment">
{%- endif -%}

{%- if cell.metadata.slide_type == 'notes' -%}
<aside class="notes">
{{ super() }}
</aside>
{%- elif cell.metadata.slide_type == 'skip' -%}
{%- else -%}
{{ super() }}
{%- endif -%}

{%- if cell.metadata.get('fragment_end', False) -%}
</div>
{%- endif -%}
{%- if cell.metadata.get('subslide_end', False) -%}
</section>
{%- endif -%}
{%- if cell.metadata.get('slide_end', False) -%}
</section>
{%- endif -%}

{%- endblock any_cell -%}

{% block header %}
<!DOCTYPE html>
<html>
<head>

<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="chrome=1" />

<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />

<title>{{resources['metadata']['name']}} slides</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<!-- General and theme style sheets -->
<link rel="stylesheet" href="{{resources.reveal.url_prefix}}/css/reveal.css">
<link rel="stylesheet" href="{{resources.reveal.url_prefix}}/css/theme/simple.css" id="theme">

<!-- If the query includes 'print-pdf', include the PDF print sheet -->
<script>
if( window.location.search.match( /print-pdf/gi ) ) {
        var link = document.createElement( 'link' );
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = '{{resources.reveal.url_prefix}}/css/print/pdf.css';
        document.getElementsByTagName( 'head' )[0].appendChild( link );
}

</script>

<!--[if lt IE 9]>
<script src="{{resources.reveal.url_prefix}}/lib/js/html5shiv.js"></script>
<![endif]-->

<!-- Loading the mathjax macro -->
{{ mathjax() }}

<!-- Get Font-awesome from cdn -->
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.css">

{% for css in resources.inlining.css -%}
    <style type="text/css">
    {{ css }}
    </style>
{% endfor %}

<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
.reveal {
  font-size: 160%;
  overflow-y: scroll;
}
.reveal pre {
  width: inherit;
  padding: 0.4em;
  margin: 0px;
  font-family: monospace, sans-serif;
  font-size: 80%;
  box-shadow: 0px 0px 0px rgba(0, 0, 0, 0);
}
.reveal pre code {
  padding: 0px;
}
.reveal section img {
  border: 0px solid black;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0);
}
.reveal i {
  font-style: normal;
  font-family: FontAwesome;
  font-size: 2em;
}
.reveal .slides {
  text-align: left;
}
.reveal.fade {
  opacity: 1;
}
.reveal .progress {
  position: static;
}
div.input_area {
  padding: 0.06em;
}
div.code_cell {
  background-color: transparent;
}
div.prompt {
  width: 11ex;
  padding: 0.4em;
  margin: 0px;
  font-family: monospace, sans-serif;
  font-size: 80%;
  text-align: right;
}
div.output_area pre {
  font-family: monospace, sans-serif;
  font-size: 80%;
}
div.output_prompt {
  /* 5px right shift to account for margin in parent container */
  margin: 5px 5px 0 0;
}
div.text_cell.rendered .rendered_html {
  /* The H1 height seems miscalculated, we are just hidding the scrollbar */
  overflow-y: hidden;
}
a.anchor-link {
  /* There is still an anchor, we are only hidding it */
  display: none;
}
.rendered_html p {
  text-align: inherit;
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

</head>
{% endblock header%}


{% block body %}
{% block pre_slides %}
<body>
{% endblock pre_slides %}

<div class="reveal">
<div class="slides">
{{ super() }}
</div>
</div>
{% block post_slides %}
<script>

require(
    {
      // it makes sense to wait a little bit when you are loading
      // reveal from a cdn in a slow connection environment
      waitSeconds: 15
    },
    [
      "{{resources.reveal.url_prefix}}/lib/js/head.min.js",
      "{{resources.reveal.url_prefix}}/js/reveal.js"
    ],

    function(head, Reveal){

        // Full list of configuration options available here: https://github.com/hakimel/reveal.js#configuration
        Reveal.initialize({
            controls: true,
            progress: true,
            history: true,

            theme: Reveal.getQueryHash().theme, // available themes are in /css/theme
            transition: Reveal.getQueryHash().transition || 'none', // default/cube/page/concave/zoom/linear/none

            // The "normal" size of the presentation, aspect ratio will be preserved
            // when the presentation is scaled to fit different resolutions. Can be
            // specified using percentage units.
            width: 822,
            height: 600, 

            // Factor of the display size that should remain empty around the content
            margin: 0.0,

            // Bounds for smallest/largest possible scale to apply to content
            minScale: 0.2,
            maxScale: 10,


            chalkboard: { 
            // optionally load pre-recorded chalkboard drawing from file
            src: "chalkboard.json",
            },
            keyboard: {
                       67: function() { RevealChalkboard.toggleNotesCanvas() },    // toggle notes canvas when 'c' is pressed
                       66: function() { RevealChalkboard.toggleChalkboard() }, // toggle chalkboard when 'b' is pressed
                       46: function() { RevealChalkboard.clear() },    // clear chalkboard when 'DEL' is pressed
                       8: function() { RevealChalkboard.reset() },    // reset chalkboard data on current slide when 'BACKSPACE' is pressed
                       68: function() { RevealChalkboard.download() }, // downlad recorded chalkboard drawing when 'd' is pressed
            },
            // Optional libraries used to extend on reveal.js
            dependencies: [
                { src: "reveal.js/plugin/chalkboard/chalkboard.js" },
                { src: "reveal.js/plugin/print-pdf/print-pdf.js" },
                { src: "reveal.js/lib/js/classList.js",
                  condition: function() { return !document.body.classList; } },
                { src: "reveal.js/plugin/notes/notes.js",
                  async: true,
                  condition: function() { return !!document.body.classList; } }
            ]
        });

        var update = function(event){
          if(MathJax.Hub.getAllJax(Reveal.getCurrentSlide())){
            MathJax.Hub.Rerender(Reveal.getCurrentSlide());
          }
        };

        Reveal.addEventListener('slidechanged', update);

        var update_scroll = function(event){
          $(".reveal").scrollTop(0);
        };

        Reveal.addEventListener('slidechanged', update_scroll);

    }
);
</script>

</body>
{% endblock post_slides %}
{% endblock body %}

{% block footer %}
</html>
{% endblock footer %}
