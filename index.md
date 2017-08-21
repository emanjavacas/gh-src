---
layout: home
permalink: /
image:
  feature: background/dunes1.JPG
---

<div class="tiles">

<div class="tile">
  <h2 class="post-title">About</h2>
  <p class="post-excerpt">I am currently a PhD student at the University of Antwerp working on a project in Computational Linguistics. Formally, I am associated with <a href="http://www.clips.ua.ac.be/">CLiPS</a> and the Antwerp Centre for Digital Humanities and Literary Criticism.</p>
</div><!-- /.tile -->

<div class="tile">
  <h2 class="post-title">Research</h2>
  <p class="post-excerpt">My current research focuses on generative and sequential (mostly RNN-backed) methods to improve on stylometric tasks as well as text-reuse detection. I am also interested in Natural Language Generation with an emphasis on Synthetic Literature.</p>
</div><!-- /.tile -->

<div class="tile">
<img src="{{ site.url }}/images/{{ site.owner.avatar }}" style="border-radius:50%; width:80%">
</div><!-- /.tile -->

<div class="tile">
  <h2 class="post-title">Contact</h2>
  <p class="post-excerpt">
	You can find me online in the following sites:<br/><br/>
	{% if site.owner.email %}<a href="mailto:{{ site.owner.email }}" class="author-social" target="_blank"><i class="fa fa-envelope-square"></i> Email</a><br/>{% endif %}
	{% if site.owner.twitter %}<a href="http://twitter.com/{{ site.owner.twitter }}" class="author-social" target="_blank"><i class="fa fa-twitter-square"></i> Twitter</a><br/>{% endif %}
	{% if site.owner.facebook %}<a href="http://facebook.com/{{ site.owner.facebook }}" class="author-social" target="_blank"><i class="fa fa-facebook-square"></i> Facebook</a><br/>{% endif %}
	{% if site.owner.google.plus %}<a href="http://plus.google.com/+{{ site.owner.google.plus }}" class="author-social" target="_blank"><i class="fa fa-google-plus-square"></i> Google+</a><br/>{% endif %}
	{% if site.owner.linkedin %}<a href="http://linkedin.com/in/{{ site.owner.linkedin }}" class="author-social" target="_blank"><i class="fa fa-linkedin-square"></i> LinkedIn</a><br/>{% endif %}
	{% if site.owner.instagram %}<a href="http://instagram.com/{{ site.owner.instagram }}" class="author-social" target="_blank"><i class="fa fa-instagram"></i> Instagram</a><br/>{% endif %}
	{% if site.owner.tumblr %}<a href="http://{{ site.owner.tumblr }}.tumblr.com" class="author-social" target="_blank"><i class="fa fa-tumblr-square"></i> Tumblr</a><br/>{% endif %}
	{% if site.owner.github %}<a href="http://github.com/{{ site.owner.github }}" class="author-social" target="_blank"><i class="fa fa-github"></i> Github</a><br/>{% endif %}
	{% if site.owner.stackoverflow %}<a href="http://stackoverflow.com/users/{{ site.owner.stackoverflow }}" class="author-social" target="_blank"><i class="fa fa-stack-overflow"></i> Stackoverflow</a><br/>{% endif %}
	{% if site.owner.lastfm %}<a href="http://lastfm.com/user/{{ site.owner.lastfm }}" class="author-social" target="_blank"><i class="fa fa-music"></i> Last.fm</a><br/>{% endif %}
	{% if site.owner.dribbble %}<a href="http://dribbble.com/{{ site.owner.dribbble }}" class="author-social" target="_blank"><i class="fa fa-dribbble"></i> Dribbble</a><br/>{% endif %}
	{% if site.owner.pinterest %}<a href="http://www.pinterest.com/{{ site.owner.pinterest }}" class="author-social" target="_blank"><i class="fa fa-pinterest"></i> Pinterest</a><br/>{% endif %}
	{% if site.owner.foursquare %}<a href="http://foursquare.com/{{ site.owner.foursquare }}" class="author-social" target="_blank"><i class="fa fa-foursquare"></i> Foursquare</a><br/>{% endif %}
	{% if site.owner.steam %}<a href="http://steamcommunity.com/id/{{ site.owner.steam }}" class="author-social" target="_blank"><i class="fa fa-steam-square"></i> Steam</a><br/>{% endif %}
  </p>
</div><!-- /.tile -->

</div><!-- /.tiles -->
