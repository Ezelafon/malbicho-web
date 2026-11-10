# Mal Bicho × AltoUrbano · Redes para balcones

Landing de redes para balcones, conectada al formulario de cotización existente. Este repositorio contiene únicamente la página de redes; el sitio general de Mal Bicho queda para una etapa posterior.

## Publicar con Cloudflare Pages

1. En Cloudflare, abrí **Workers y Pages → Crear aplicación → Pages → Conectar a Git**.
2. Seleccioná `Ezelafon/malbicho-web` y la rama `main`.
3. Configurá:

| Campo | Valor |
|---|---|
| Framework | Ninguno |
| Comando de compilación | `python3 build.py` |
| Directorio de salida | `dist` |
| Directorio raíz | Raíz del repositorio |

4. Publicá. La landing se sirve en `/` y `/redes/`.
5. Para fijar el dominio de la vista previa compartida, agregá la variable `SITE_URL` con el origen definitivo, por ejemplo `https://malbicho.ar`, sin `/redes`. Volvé a compilar al cambiarla.

Sin `SITE_URL`, Cloudflare aporta `CF_PAGES_URL` y el build utiliza esa dirección. Fuera de Cloudflare, el valor predeterminado es `https://malbicho.ar`.

**El repositorio no activa por sí solo el dominio ni publica una web.** La conexión a Pages y el dominio se configuran en Cloudflare. Antes de conectar un dominio que ya sirve otra web, revisá su configuración. Los registros de correo no forman parte de este proyecto.

## Archivos

- `public/index.html`: textos, diseño y enlace al formulario.
- `public/assets/balcon.svg`: esquema ilustrativo para medir las aberturas.
- `public/assets/marcas.png.b64`: logos existentes de Mal Bicho y AltoUrbano.
- `public/assets/compartir.png.b64`: imagen de 1200 × 630 para la vista previa social.
- `build.py`: prepara los archivos de publicación en `dist/`.

Las dos imágenes PNG están guardadas en Base64. El build las convierte automáticamente a PNG normales. No hay que copiar esos textos al HTML ni convertirlos manualmente.

## Uso local

```sh
python3 build.py
python3 -m http.server 8000 --directory dist
```

Abrí `http://localhost:8000/redes/`. Para probar otros metadatos, definí `SITE_URL` antes de compilar.

## Formulario y automatización

Los botones dirigen a `https://forms.gle/61QCLLvnZDWCSCRT9`. La captura de datos, el cálculo, la confirmación y los correos continúan en Google Forms, Sheets y Apps Script. La página no almacena datos de interesados, ni contiene credenciales, precios internos o respuestas de clientes.

La selección de la red y el presupuesto final se confirman luego del relevamiento. Los rangos de la automatización se expresan sin IVA.

## Comprobar después de publicar

- Abrir `/redes/` en celular y computadora.
- Probar el formulario desde una cuenta externa o ventana privada.
- Confirmar que la imagen indicada por `og:image` se abre públicamente.
- Compartir el enlace público por WhatsApp y verificar la tarjeta. La presentación final depende de WhatsApp y su caché.

## Modificar la página

Editá `public/index.html` y guardá los cambios en `main`. Una vez conectado Pages, los commits de esa rama disparan la publicación. No se requiere Node, paquetes externos ni base de datos.
