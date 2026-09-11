# Mondrianiac

A small, free playground for line, color, proportion, and balance, inspired by Piet Mondrian.

**Website:** https://conrad-jacobs.github.io/mondrianiac/

## Use the studio

- Select a color, then click an area. Paint fills every connected open space.
- Drag interior bars to reshape cells. There is no automatic snapping. Touching segments remain independent unless they complete a side of a rectangular cell, in which case they form one movable divider. True overlaps merge, including into the protected outer frame.
- Dragging preserves existing rectangular cells. Deletion may leave irregular areas; adding or moving bars repairs them. A repaired rectangle takes its predominant existing color and can then be repainted.
- Drag the frame inward to compress neighboring cells while keeping minimum spacing.
- Choose a horizontal or vertical line tool, then click open space to add a bar.
- Right-click an interior bar to remove the segment between adjacent perpendicular intersections. The color occupying the largest area fills the joined cell; exact ties are decided randomly.
- Center (on the right) recenters the picture without resizing it or changing its composition. It can be undone.
- Refresh starts a new composition; Undo can restore the previous picture.
- Undo with the button or Command/Ctrl+Z. Escape leaves line mode.
- Save image downloads a PNG of the visible artwork inside the editing frame, with no edge bars.

The thin boundary around the workspace marks its maximum extent. The light gray frame inside it is a draggable editing guide, excluded from saved pictures. Interior bars remain black.

## Files and local preview

Open `index.html` in a browser. There are no installation or build steps. CSS and JavaScript are contained in that file; the portrait and favicon are in `assets/`.

The app runs entirely in the browser, with no backend, account requirement, external fonts, analytics, or runtime dependencies. Paintings are kept in memory until downloaded; refreshing starts a new composition.

## Hosting

GitHub Actions publishes both branches together, using `.github/workflows/pages.yml`. Pages settings must use **GitHub Actions** as the source.

| Version | Branch | URL | Local folder |
| --- | --- | --- | --- |
| Public | `main` | https://conrad-jacobs.github.io/mondrianiac/ | `mondrianiac` |
| Development | `dev` | https://conrad-jacobs.github.io/mondrianiac/dev/ | `mondrianiac-dev` |

The development site is publicly accessible, marked with a yellow banner, and requests that search engines not index it. It is not a private staging area. Both folders use `index.html`; do not edit the ignored `mondrian_7.html` reference.

### Test a change

Edit `mondrianiac-dev/index.html`, then open that file in your browser for a local preview. To update the online testing site:

```sh
cd /Users/neurorobots/MEGA/JACOB/HTML_FUN/mondrianiac-dev
git add index.html  # add other changed files explicitly if needed
git commit -m "Describe the change"
git push origin dev
```

### Release a tested change

With both folders' changes committed:

```sh
cd /Users/neurorobots/MEGA/JACOB/HTML_FUN/mondrianiac
git pull --ff-only origin main
git merge dev
git push origin main
```

This publishes the tested development changes to the public site. If Git reports a conflict, resolve it before committing and pushing. After changes made directly on `main`, bring them into development with `git merge main` in `mondrianiac-dev`, then `git push origin dev`.

Every deployment fetches both branches, so a development push keeps the public site on `main`. Check the repository’s Actions tab for deployment progress, then reload the browser. The app's Refresh button starts a new painting; it does not reload the website.

All asset paths are relative, so the same files work at a GitHub Pages project URL or on a custom domain. A domain can be configured later through the repository's Pages settings; no app rewrite is needed.

- [GitHub Pages publishing documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Custom domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages)

## Credits

> “It is so hard, the work.”

Piet Mondrian, as recalled by Charmion von Wiegand, quoted in Nicholas Fox Weber, *Mondrian: His Life, His Art, His Quest for the Absolute* (2024), Knopf Doubleday. Quotation and bibliographic attribution supplied by the project creator.

Portrait: Piet Mondrian in his New York studio, 1942. Photograph by Arnold Newman; collection RKD, The Hague. Source: [Villa Mondriaan timeline](https://villamondriaan.nl/en/timeline/). The source image is stored locally in `assets/mondrian-in-his-studio.jpg`.
