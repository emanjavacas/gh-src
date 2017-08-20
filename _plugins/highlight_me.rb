# coding: utf-8

Jekyll::Hooks.register :pages, :pre_render do |page|
  page.content.gsub!('Manjavacas Arévalo, Enrique', '<strong>Manjavacas Arévalo, Enrique</strong>')
end
