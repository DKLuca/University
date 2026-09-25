---
fonte: "17_Frontend-Development-CSS-Grid-Responsive.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Fundamentals of Web Applications
Frontend Development: Grid and Responsive
Layout in CSS
Lecture 17 and 18 – May 7 and 13, 2026
Michael Soprano - michael.soprano@uniud.it
University of Udine - Department of Mathematics,
Computer Science, and Physics (DMIF)
                                                   1/59
Outline
1. Two-Dimensional Layouts
2. Responsive Layout
3. Positioning and Layers




                             2/59
Two-Dimensional Layouts




Layout Context Recap
   CSS layout usually starts from the normal flow
   Flexbox and Grid are applied to a container
   Only the container’s direct children become layout items
   Flexbox is strongest for one-dimensional arrangements
   Grid is designed for layouts that need rows and columns together



                                                                      3/59
Grid Rows and Columns
  Grid arranges items inside a two-dimensional structure
  The container defines columns , rows , tracks , and gaps
  The direct children become grid items
  Grid items can occupy one cell or span multiple cells
  Container properties define the structure, while item properties define
  placement
Role        Examples
Container   grid-template-columns , grid-template-rows , grid-template-areas , gap
Item        grid-column , grid-row , grid-area


                                                                                     4/59
Grid Structure Overview
                                                           Grid Line
                              1         2              3                 4                5               6
                          1

                                                                                              Grid Cell

                          2

                                                                       Grid Track (Row)

                          3




                          4                   Grid
                                             Track
                                            (Column)

                          5                                                         Grid Area




                          6

                                                                                                              5/59
Main parts of a grid layout structure
Column Tracks: grid-template-columns
    grid-template-columns defines the column structure
   The fr unit distributes available space between flexible columns
   Equal fr values create equal-width columns
   Additional rows can be created automatically when more items are added
.gallery {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1rem;
}



                                                                     6/59
Adaptive Columns: auto-fit and minmax()
   A fixed number of columns can become too narrow on small screens
    auto-fit creates as many columns as fit
    minmax(220px, 1fr) keeps each column readable before it grows
   The grid adapts without changing the HTML structure
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}



                                                                      7/59
Automatic Placement
 Grid items do not always need explicit coordinates
 By default, the browser places items into the next available grid cell
 Additional rows are created automatically when more items are added
 Repeated content such as galleries and card lists can follow this
 automatic flow



                                                                      8/59
Example: Source Code
   Sample resource : AU_grid-gallery/index.html
   The gallery contains several cards with the same HTML structure
<!-- Head omitted for brevity -->
<body>
  <main class="page">
    <h1>Course Topics</h1>

    <section class="gallery">
      <article class="card">
        <h2>HTML Structure</h2>
        <p>Semantic elements define the meaning of the content.</p>
      </article>
      <article class="card">
        <h2>CSS Layout</h2>
        <p>Layout rules arrange boxes into readable interfaces.</p>
      </article>
      <!-- Additional cards omitted for brevity -->
    </section>
  </main>
</body>                                                               9/59
Example: Source Code
   Sample resource : AU_grid-gallery/style.css
    auto-fit and minmax() create adaptive columns for the gallery
   The browser places the cards automatically into the available grid cells
body { margin: 0; font-family: Arial, Helvetica, sans-serif; line-height: 1.5; }

.page {
  max-width: 960px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}

.card { padding: 1rem; border: 1px solid #cccccc; background-color: #eaf3ff; }     10/59
Example: Result
     The cards are placed automatically into grid cells
     The browser decides how many columns fit in the available container
     width
     New rows are created automatically when there are more cards
     The HTML stays simple while Grid controls the visual structure




                                                                       11/59
A responsive card gallery created with CSS Grid
Automatic and Explicit Placement
 Grid can place repeated items automatically into the available cells
 Some items can also receive explicit placement rules
 Explicit placement gives an item a different span or visual region
 The same grid can combine automatic flow and selected manual placement




                                                                 12/59
Item Spans: grid-column and grid-row
   A grid item can span across multiple columns or rows
   Line numbers identify where the item starts and where it ends
    grid-column controls the horizontal span
    grid-row controls the vertical span

.feature { grid-column: 1 / 3; }

.sidebar { grid-row: 2 / 4; }




                                                                   13/59
Named Layout Areas
   Line numbers are precise, but they can become hard to read in larger
   layouts
   Some layouts read more clearly as named areas
    grid-template-areas describes the layout as a small textual map
   The map is written on the grid container
.page-layout {
  display: grid;
  grid-template-areas:
    "header header"
    "main sidebar";
  grid-template-columns: 2fr 1fr;
}

                                                                      14/59
Reading Area Maps
   Each quoted line represents one grid row
   Each name inside a line represents one grid cell
   Repeated names create a larger layout area
    grid-template-columns gives sizes to the mapped columns

                       Column 1                  Column 2
Row 1                  header                    header
Row 2                  main                      sidebar


grid-template-areas:
  "header header"
  "main sidebar";

                                                              15/59
Area Spans and Empty Cells
   A named area spans exactly the cells where its name appears
   All cells with the same name must form one contiguous rectangle
   Use . when a cell should be intentionally empty
   The map should show the full intended visual structure
grid-template-areas:
  "header header header"
  "main main sidebar";

/* With an empty cell */
grid-template-areas:
  "header header ."
  "main sidebar .";


                                                                     16/59
Assigning Items to Areas
   The area map defines the available layout areas
   Each grid item is assigned to one named area with grid-area
   The item occupies all cells where that area name appears
   Changing the map can rearrange the layout without changing the HTML
   structure
.page-layout {
  display: grid;
  grid-template-areas:
    "header header"
    "main sidebar";
  grid-template-columns: 2fr 1fr;
  gap: 1rem;
}

.header { grid-area: header; }
.main { grid-area: main; }
.sidebar { grid-area: sidebar; }                                   17/59
Semantic Order and Layout Areas
   Semantic elements describe the meaning of the content
   Grid area names describe the visual regions used by CSS
   Similar names make the relationship between semantics and layout easier
   to read
   Visual placement does not change the underlying source order
   Use Grid to improve layout, not to repair an incorrect document structure
<header class="header">...</header>
<section class="main">...</section>
<aside class="sidebar">...</aside>


.header { grid-area: header; }
.main { grid-area: main; }
.sidebar { grid-area: sidebar; }
                                                                      18/59
Example: Source Code
    Sample resource : AV_grid-page-regions/index.html
    The document uses semantic elements for the main content regions
    CSS will assign these elements to named layout areas
<!-- Head omitted for brevity -->
<body>
  <main class="page-layout">
    <header class="header">
       <h1>Course Dashboard</h1>
    </header>

    <section class="main">
      <h2>Current Topic</h2>
      <p>Modern CSS layout combines structure, spacing, and responsive behavior.</p>
    </section>

    <aside class="sidebar">
      <h2>Resources</h2>
      <ul>
        <li>Slides</li>
        <li>Examples</li>
        <li>Exercises</li>
      </ul>
    </aside>
  </main>                                                                              19/59
</body>
Example: Source Code
   Sample resource : AV_grid-page-regions/style.css
   The container defines the visual map of the layout
   Each direct child is assigned to one named grid area
.page-layout {
  max-width: 900px;
  margin: 2rem auto;
  display: grid;
  grid-template-areas:
    "header header"
    "main sidebar";
  grid-template-columns: 2fr 1fr;
  gap: 1rem;
}

.header { grid-area: header; }
.main { grid-area: main; }
.sidebar { grid-area: sidebar; }
                                                          20/59
Example: Result
    The header spans both columns
    The main content and sidebar occupy separate grid areas
    The HTML describes the content structure
    CSS defines the two-dimensional visual arrangement




                                                                  21/59
Named grid areas make layout regions easier to arrange and read
Flexbox and Grid
  Flexbox arranges items mainly along one main axis
  Grid controls rows and columns together
  Both systems are applied to a container
  The choice depends on the structure the layout needs
Need                                                     Better Fit
Navigation links in one row                              Flexbox
Toolbar regions                                          Flexbox
Card gallery                                             Grid
Page regions with rows and columns                       Grid

                                                                      22/59
Responsive Layout




Available Space Changes
   The same component may be rendered in very different available spaces
   A layout can be readable at one width and cramped at another
   The HTML structure should not need to change for each screen size
   CSS can adapt the visual arrangement when space changes




                                                                   23/59
Responsive Layout
 A responsive layout adapts its visual arrangement to the available space
 The goal is to keep content readable , usable , and visually stable
 A different arrangement is introduced only when it improves the
 component
 Responsive design is therefore based on layout needs , not device names



                                                                    24/59
Viewport and Containers
 The viewport is the visible area of the browser window
 A component is also rendered inside a specific container
 Available space can depend on the viewport, the container, or both
 Responsive layout considers both the page and the component




                                                                      25/59
Responsive Breakpoints
 A breakpoint is the condition where CSS changes the layout
 It marks the point where the current arrangement no longer works well
 Different components may need different breakpoints
 In CSS, breakpoints are commonly implemented with media queries




                                                                   26/59
Media Queries: @media
   A media query applies CSS only when a condition is true
   The rules inside @media are used only when the query matches
   The condition can test width , height , orientation , and other media
   features
   Width conditions are the most common starting point for responsive
   layout
@media (condition) {
  selector {
    property: value;
  }
}

                                                                           27/59
Width-Based Conditions
    min-width applies rules from a given width upward
    max-width applies rules up to a given maximum width
   A range can target widths between two values
   A mobile-first layout commonly uses min-width
@media (min-width: 720px) {
  /* Rules for viewports at least 720px wide */
}

@media (max-width: 719px) {
  /* Rules for viewports up to 719px wide */
}

@media (min-width: 720px) and (max-width: 1024px) {
  /* Rules for an intermediate width range */
}
                                                          28/59
Mobile-First Strategy
   In a mobile-first strategy, the base CSS describes the narrow layout
   Wider layouts are added progressively with min-width queries
   This keeps the first layout simple
   It also avoids overriding many desktop-oriented rules
.feature-card {
  display: grid;
  gap: 1rem;
}

@media (min-width: 720px) {
  .feature-card {
    grid-template-columns: 180px 1fr;
  }
}

                                                                          29/59
Bootstrap Grid Pattern
    Many CSS frameworks adopt a mobile-first responsive strategy
    In Bootstrap, the smallest layout is defined first
    Breakpoint-specific classes add wider layouts progressively
    The same idea appears in custom CSS with min-width media queries
<div class="row">
  <article class="col-12 col-md-6 col-lg-4">Card</article>
  <article class="col-12 col-md-6 col-lg-4">Card</article>
  <article class="col-12 col-md-6 col-lg-4">Card</article>
</div>



                                                                        30/59
col-12 , col-md-6 , and col-lg-4 describe progressively wider layouts
Mobile-First Design




                                                                                       31/59
Mobile-first design starts from narrow screens and progressively enhances the layout
Example: Source Code
   Sample resource : AW_responsive-media-card/index.html
   The card contains an image, text content, and an action link
<!-- Head omitted for brevity -->
<body>
  <main class="page">
    <article class="feature-card">
       <img src="images/layout-preview.svg" alt="Preview of a responsive layout">

      <div class="feature-content">
        <p class="label">Frontend Development</p>
        <h1>Responsive Components</h1>
        <p>
          A component can change its visual layout while keeping
          the same HTML structure.
        </p>
        <a href="#">View materials</a>
      </div>
    </article>
  </main>
</body>                                                                             32/59
Example: Mobile-First CSS
   Sample resource : AW_responsive-media-card/style.css
   The base rules create a narrow layout
   The media query adds a wider layout from 720px upward
.feature-card {
  /* Base layout: one-column grid for narrow viewports */
  display: grid;
  gap: 1rem;
}

@media (min-width: 720px) {
  .feature-card {
    /* Wider layout: fixed media column and flexible text column */
    grid-template-columns: 180px 1fr;
  }
}

                                                                      33/59
Example: Result
     Below 720px , the card remains a vertical layout
     From 720px upward, the card becomes a two-column layout
     The image occupies the first column
     The text content occupies the flexible second column




                                                                      34/59
The same card changes from a vertical layout to a two-column layout
Responsive Media
   Responsive layout is not only about arranging boxes
   Images and videos also occupy space inside components
   Their intrinsic size can be larger than the available container space
   Responsive media rules keep media inside flexible layouts
img,
video {
  max-width: 100%;
  height: auto;
}



                                                                           35/59
Fluid Images
   A fluid image scales with its container
    max-width: 100% prevents the image from becoming wider than the
   container
    height: auto preserves the original aspect ratio
   The full image remains visible while it scales down
img {
  max-width: 100%;
  height: auto;
}



                                                                      36/59
Stable Media Frames: aspect-ratio and object-fit
   Some components need media with a consistent visual shape
    aspect-ratio reserves predictable layout space
    object-fit: cover fills the frame and may crop the content
    object-fit: contain shows the full content and may leave empty space

.card img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}



                                                                       37/59
Choosing the Right Media Rule
 Use fluid media when the full content should remain visible
 Use a stable frame when the component needs a consistent shape
 Use object-fit: contain when cropping would remove important content
 Use object-fit: cover when visual consistency matters more than full
 visibility



                                                                 38/59
Example: Source Code
   Sample resource : AX_responsive-media-rules/index.html
   The example compares a fluid image and a framed image
   Both images use the same source file, but different CSS rules
<!-- Head omitted for brevity -->
<body>
  <main class="page">
    <h1>Responsive Media Rules</h1>

    <section class="media-grid">
      <article class="media-card">
        <h2>Fluid Image</h2>
        <img class="fluid-image" src="images/campus.jpg" alt="Tall university building">
        <p>The full image remains visible and scales with the container.</p>
      </article>

      <article class="media-card">
        <h2>Framed Image</h2>
        <img class="framed-image" src="images/campus.jpg" alt="Tall university building">
        <p>The image fills a stable frame and may be cropped.</p>
      </article>
    </section>
  </main>                                                                                   39/59
</body>
Example: Source Code
   Sample resource : AX_responsive-media-rules/style.css
    .fluid-image prioritizes full visibility
    .framed-image prioritizes a stable component shape

.fluid-image {
  max-width: 100%;
  height: auto;
}

.framed-image {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}


                                                           40/59
Example: Result
    The fluid image keeps the full picture visible
    The framed image keeps a consistent rectangular shape
     object-fit: cover fills the frame by cropping if needed
    The right rule depends on the role of the media in the component




                                                                                         41/59
Fluid media preserves the full image, while framed media preserves the component shape
Responsive Layout Checklist
 Start from a readable small-screen structure
 Use Flexbox or Grid to arrange related components
 Add breakpoints when the layout actually needs to change
 Keep media items inside their containers
 Choose fluid media or framed media based on the media role



                                                              42/59
Positioning and Layers




Special Placement Problems
   Flexbox and Grid arrange the main layout structure
   Some interface elements need more specific placement
   A badge may sit in the corner of a card
   A button may stay fixed near the edge of the viewport
   A label may remain visible while the page scrolls



                                                           43/59
Positioning Mode: position
    static is the default mode, and the element follows the normal flow
   Other values create positioned elements
   Positioned elements can use top , right , bottom , and left
   The meaning of those offsets depends on the selected positioning mode
   Positioning should not replace Flexbox or Grid for ordinary layout
   structure
.badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
}

                                                                      44/59
Local Reference: relative
    position: relative keeps the element in the normal flow
   Offsets move the element visually from its normal-flow position
   The original space is still preserved
   It often creates a local positioning reference for absolutely positioned
   children
.card {
  position: relative;
}



                                                                        45/59
Local Overlay: absolute
    position: absolute removes the element from the normal flow
   The element is positioned relative to the nearest positioned ancestor
   Offsets place the element from the edges of that positioning reference
   This pattern places badges, icons, tooltips, and small overlays inside a
   component
.card {
  position: relative;
}

.badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
}
                                                                       46/59
Viewport and Scroll Placement
    position: fixed anchors an element to the viewport
   The element stays in the same visual position while the document scrolls
    position: sticky starts in the normal flow
   A sticky element becomes fixed only after a scroll threshold is reached
   Both modes should be checked carefully because they can cover content
.help-button {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
}

.section-label {
  position: sticky;
  top: 0;
}
                                                                       47/59
Layer Order: z-index
   Positioned elements can overlap other elements
   z-index controls the stacking order
   Higher values appear in front of lower values
   Use it only when overlap is intentional
.card {
  position: relative;
}

.badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  z-index: 1;
}

                                                    48/59
Example: Source Code
   Sample resource : AY_positioned-badge-card/index.html
   The card list uses Flexbox for the main layout
   The badge is positioned inside one card as a local overlay
<!-- Head and body omitted for brevity -->
<main class="page">
  <section class="card-list">
    <article class="card">
      <span class="badge">New</span>
      <h1>Modern Layout</h1>
      <p>Flexbox arranges the card list, while positioning places the badge.</p>
      <a href="#">Open notes</a>
    </article>

    <article class="card">
      <h1>Responsive Media</h1>
      <p>Other cards follow the same flex layout.</p>
      <a href="#">View example</a>
    </article>
  </section>                                                                       49/59
</main>
Example: Flex Layout
   Sample resource : AY_positioned-badge-card/style.css
    .card-list creates the Flexbox layout
    .card becomes both a flex item and a local positioning reference

.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  position: relative;
  flex: 1 1 18rem;
  padding: 1.5rem;
  border: 1px solid #cccccc;
}

                                                                       50/59
Example: Positioned Badge
   Sample resource : AY_positioned-badge-card/style.css
    .badge is positioned relative to the nearest positioned ancestor
   In this example, that ancestor is .card
    top and right place the badge from the card’s top-right corner

.badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  padding: 0.25rem 0.6rem;
  background-color: #1f4e79;
  color: #ffffff;
  font-weight: 700;
  z-index: 1;
}

                                                                       51/59
Example: Result
     Flexbox arranges the cards as layout items
     The badge appears as a small overlay inside one card
     Positioning affects the badge, not the whole card list
     The main layout remains controlled by Flexbox




                                                                                          52/59
Flexbox arranges the cards, while absolute positioning places the badge inside one card
Reading the Example
 The card list remains a normal Flexbox layout
 Each card keeps its own space inside that layout
  position: relative gives the card a local reference
  position: absolute lets the badge use that reference for local placement
  top , right , and z-index affect only the badge’s overlay behavior




                                                                      53/59
Positioning Summary
 Use Flexbox or Grid for the main layout structure
 Use relative to create a local positioning reference
 Use absolute for local overlays inside a component
 Use fixed and sticky for viewport or scroll-aware elements
 Use z-index only when elements intentionally overlap



                                                              54/59
Layout Decisions
 Start from meaningful HTML structure
 Let normal flow handle simple arrangements
 Use Flexbox for mainly one-dimensional groups
 Use Grid for structures based on rows and columns
 Use responsive rules when available space changes the layout
 Use positioning only for special placement , overlays, and layers


                                                                     55/59
Looking Ahead: Selectors
 Layout rules depend on selecting the right elements
 Simple selectors cover many basic rules
 More complex interfaces need more precise selection patterns
 Advanced selectors target states, combinations, and repeated structures
 Better selectors make stylesheets more expressive and easier to maintain



                                                                    56/59
Bibliography
 Duckett, J. (2011). HTML and CSS: Design and Build Websites. John Wiley &
 Sons
    Chapter 15: Layout
    Chapter 17: HTML5 Layout
 MDN Web Docs. Basic concepts of grid layout
    https://developer.mozilla.org/en-
    US/docs/Web/CSS/CSS_grid_layout/Basic_concepts_of_grid_layout
 MDN Web Docs. Grid template areas
    https://developer.mozilla.org/en-
    US/docs/Web/CSS/CSS_grid_layout/Grid_template_areas
                                                                       57/59
Bibliography (cont.)
  MDN Web Docs. Media queries
     https://developer.mozilla.org/en-
     US/docs/Web/CSS/CSS_media_queries/Using_media_queries
  MDN Web Docs. Responsive design
     https://developer.mozilla.org/en-
     US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
  Bootstrap Documentation. Grid system
     https://getbootstrap.com/docs/5.3/layout/grid/


                                                                       58/59
Bibliography (cont.)
  MDN Web Docs. position
     https://developer.mozilla.org/en-US/docs/Web/CSS/position
  MDN Web Docs. z-index
     https://developer.mozilla.org/en-US/docs/Web/CSS/z-index
  MDN Web Docs. aspect-ratio
     https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio
  MDN Web Docs. object-fit
     https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit

                                                                     59/59
