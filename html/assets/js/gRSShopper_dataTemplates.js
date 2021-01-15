
	function pageSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typepage" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="RSS">RSS</a>
					<option value="HTML">HTML</a>
					<option value="CSS">CSS</a>
					<option value="XML">XML</a>
					<option value="JS">JS</a>
					<option value="email">email</a>
					<option value="TEXT">TEXT</a>
					<option value="XSL">XSL</a>
					<option value="JSON">JSON</a>
							</select></p>
		</div>`;
	};

	
	function aSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
		</div>`;
	};

	
	function projectSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>category <select name="category" id="categoryproject" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function postSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>category <select name="category" id="categorypost" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="OLDaily">OLDaily</a>
							</select></p>
				<p>type <select name="type" id="typepost" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="shownotes">shownotes</a>
					<option value="course">Course</a>
					<option value="article">Article</a>
					<option value="comment">Comment</a>
					<option value="preview">Preview</a>
					<option value="announcement">Announcement</a>
					<option value="musing">Musing</a>
					<option value="link">Link</a>
							</select></p>
				<p>genre <select name="genre" id="genrepost" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',genre:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>field <select name="field" id="fieldpost" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',field:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Thumbnail">Thumbnail</a>
					<option value="Enclosure">
Enclosure</a>
					<option value="Audio">
Audio</a>
					<option value="Other Image">
Other Image</a>
					<option value="Display">
Display</a>
					<option value="Genre">Genre</a>
					<option value="Interview">Interview</a>
							</select></p>
		</div>`;
	};

	
	function placeSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>category <select name="category" id="categoryplace" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function fileSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typefile" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Thumbnail">Thumbnail</a>
					<option value="Illustration">Illustration</a>
					<option value="Document">Document</a>
					<option value="Enclosure">Enclosure</a>
					<option value="Slides">Slides</a>
					<option value="Audio">Audio</a>
							</select></p>
		</div>`;
	};

	
	function channelSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>twitterstatus <select name="twitterstatus" id="twitterstatuschannel" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',twitterstatus:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>status <select name="status" id="statuschannel" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',status:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>extype <select name="extype" id="extypechannel" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',extype:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>mastodonstatus <select name="mastodonstatus" id="mastodonstatuschannel" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',mastodonstatus:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function authorSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typeauthor" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Person">Person</a>
					<option value="Organization">Organization</a>
							</select></p>
		</div>`;
	};

	
	function personSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>status <select name="status" id="statusperson" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',status:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="admin">admin</a>
					<option value="registered">registered</a>
					<option value="anon">anon</a>
							</select></p>
		</div>`;
	};

	
	function mediaSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typemedia" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="audio">audio</a>
					<option value="video">video</a>
					<option value="document">document</a>
					<option value="image">image</a>
							</select></p>
				<p>mimetype <select name="mimetype" id="mimetypemedia" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',mimetype:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function optlistSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typeoptlist" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function companySearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>category <select name="category" id="categorycompany" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="publisher">Publisher</a>
					<option value="consultant">Consultant</a>
					<option value="platform">Platform</a>
					<option value="hardware">Computers and Hardware</a>
					<option value="analysts">Analysts</a>
					<option value="retail">Retail</a>
					<option value="AI">AI</a>
					<option value="training">Training and Skills</a>
					<option value="media">News Media</a>
					<option value="software">Software</a>
					<option value="services">Services</a>
					<option value="custom">Custom Content</a>
					<option value="content">Content</a>
							</select></p>
				<p>genre <select name="genre" id="genrecompany" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',genre:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="political">Political</a>
					<option value="communication">Communication</a>
					<option value="general">General</a>
					<option value="education">Education</a>
					<option value="financial">Financial</a>
					<option value="technology">Technology</a>
					<option value="philosophy">Philosophy</a>
					<option value="Academic">Academic</a>
					<option value="mooc">Mooc</a>
					<option value="commerce">Business and commerce</a>
							</select></p>
		</div>`;
	};

	
	function conceptSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typeconcept" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="intuitive">Intuitive</a>
							</select></p>
				<p>category <select name="category" id="categoryconcept" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="concept">Concept</a>
					<option value="License">License</a>
					<option value="model">Model</a>
					<option value="theory">Theory</a>
					<option value="framework">Framework</a>
					<option value="activity">Activity</a>
					<option value="tool">Tool</a>
					<option value="Curriculum">Curriculum</a>
					<option value="type">Type</a>
					<option value="standard">Standard or specification</a>
					<option value="person">Person</a>
					<option value="Algorithm">Algorithm</a>
							</select></p>
				<p>genre <select name="genre" id="genreconcept" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',genre:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="political">Political</a>
					<option value="culture">Culture</a>
					<option value="general">General</a>
					<option value="psychology">Psychology</a>
					<option value="gender">Gender</a>
					<option value="education">Education</a>
					<option value="technology">Technology</a>
					<option value="philosophy">Philosophy</a>
					<option value="commerce">Business and commerce</a>
							</select></p>
		</div>`;
	};

	
	function organizationSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typeorganization" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Trust">Trust</a>
					<option value="SIG">SIG</a>
					<option value="Board">Board</a>
					<option value="Syndicate">Syndicate</a>
					<option value="Foundation">Foundation</a>
					<option value="Lab">Lab</a>
					<option value="Club">Club</a>
					<option value="Federation">Federation</a>
					<option value="Movement">Movement</a>
					<option value="Organization">Organization</a>
					<option value="institute">Institute</a>
					<option value="System">System</a>
					<option value="Centre">Centre</a>
					<option value="Network">Network</a>
					<option value="Alliance">Alliance</a>
					<option value="Coalition">Coalition</a>
					<option value="Commission">Commission</a>
					<option value="Incubator">Incubator</a>
					<option value="group">Group</a>
					<option value="Union">Union</a>
					<option value="Association">Association</a>
					<option value="Committee">Committee</a>
					<option value="Consortium">Consortium</a>
					<option value="Society">Society</a>
							</select></p>
				<p>category <select name="category" id="categoryorganization" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Political">Political</a>
					<option value="International">International</a>
					<option value="Research">Research</a>
					<option value="Education">Education</a>
					<option value="Media">Media</a>
					<option value="Community">Community</a>
					<option value="Trade/Commerce">Trade/Commerce</a>
					<option value="Health">Health</a>
					<option value="enviornment">Enviornment</a>
					<option value="business">Business</a>
					<option value="NGO">NGO</a>
					<option value="Government">Government</a>
					<option value="Cooperative">Cooperative</a>
					<option value="Technical">Technical</a>
					<option value="non-profit">Non-profit</a>
					<option value="Academic">Academic</a>
					<option value="Industry">Industry</a>
							</select></p>
				<p>genre <select name="genre" id="genreorganization" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',genre:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function journalSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>genre <select name="genre" id="genrejournal" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',genre:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function fieldSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typefield" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="text">text</a>
					<option value="select">select</a>
					<option value="textarea">textarea</a>
							</select></p>
		</div>`;
	};

	
	function topicSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>status <select name="status" id="statustopic" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',status:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>type <select name="type" id="typetopic" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function presentationSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>category <select name="category" id="categorypresentation" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>catdetails <select name="catdetails" id="catdetailspresentation" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',catdetails:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Poster">Poster</a>
					<option value="Panel">Panel</a>
					<option value="Interview">Interview</a>
					<option value="Workshop">Workshop</a>
					<option value="Lecture">Lecture</a>
					<option value="Internal Presentation">Internal Presentation</a>
					<option value="Seminar">Seminar</a>
					<option value="Keynote">Keynote</a>
					<option value="Class">Class</a>
					<option value="Debate">Debate</a>
							</select></p>
		</div>`;
	};

	
	function linkSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>status <select name="status" id="statuslink" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',status:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Retired">Retired</a>
					<option value="Unread">Unread</a>
					<option value="Stale">Stale</a>
					<option value="Posted">Posted</a>
					<option value="Fresh">Fresh</a>
					<option value="Starred">Starred</a>
							</select></p>
				<p>category <select name="category" id="categorylink" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>type <select name="type" id="typelink" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>genre <select name="genre" id="genrelink" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',genre:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function feedSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>status <select name="status" id="statusfeed" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',status:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="R">Retired</a>
					<option value="O">On Hold</a>
					<option value="B">Unlinked</a>
					<option value="A">Approved</a>
							</select></p>
				<p>section <select name="section" id="sectionfeed" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',section:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="other">Other</a>
					<option value="news media">News Media</a>
					<option value="podcast">Podcast</a>
					<option value="journal">Journal</a>
					<option value="blog">Blog</a>
							</select></p>
				<p>type <select name="type" id="typefeed" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Atom">Atom</a>
					<option value="RSS 1.0">RSS 1.0</a>
					<option value="RSS 2.0">RSS 2.0</a>
					<option value="Not Harvesting">Not Harvesting</a>
					<option value="YouTube">YouTube</a>
					<option value="Twitter">Twitter</a>
					<option value="RSS 0.91">RSS 0.91</a>
					<option value="OAI">OAI</a>
					<option value="JSON">JSON</a>
					<option value="Facebook">Facebook</a>
							</select></p>
				<p>category <select name="category" id="categoryfeed" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Language">Language</a>
					<option value="K12">K12</a>
					<option value="media">Media</a>
					<option value="edubloggers">Education Blogs</a>
					<option value="Ed Tech">Ed Tech</a>
					<option value="Higher Ed">Higher Ed</a>
					<option value="ideas">Ideas</a>
					<option value="design">Design</a>
					<option value="news---ed">Education News</a>
					<option value="cyberculture">Cyberculture</a>
					<option value="Corporate">Corporate</a>
							</select></p>
				<p>genre <select name="genre" id="genrefeed" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',genre:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function workSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typework" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="fiction">Fiction</a>
					<option value="declaration">Declaration</a>
					<option value="news">News</a>
					<option value="research">Research</a>
					<option value="reference">Reference</a>
					<option value="science">Science</a>
					<option value="non-fiction">Non-fiction</a>
					<option value="agreement">Agreement</a>
					<option value="educational">Educational</a>
					<option value="philosophy">Philosophy</a>
					<option value="tech">Tech</a>
					<option value="policy">Policy</a>
							</select></p>
				<p>category <select name="category" id="categorywork" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="course">Course</a>
					<option value="website">website</a>
					<option value="video">Video</a>
					<option value="database">Database</a>
					<option value="book">Book</a>
					<option value="Dashboard">Dashboard</a>
					<option value="podcast">Podcast</a>
					<option value="publication">Publication</a>
					<option value="TV">TV</a>
					<option value="">movie</a>
					<option value="">Movie</a>
					<option value="report">Report</a>
					<option value="audio">Audio</a>
							</select></p>
		</div>`;
	};

	
	function taskSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>status <select name="status" id="statustask" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',status:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function eventSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>status <select name="status" id="statusevent" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',status:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>category <select name="category" id="categoryevent" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>type <select name="type" id="typeevent" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function threadSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>twitterstatus <select name="twitterstatus" id="twitterstatusthread" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',twitterstatus:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>status <select name="status" id="statusthread" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',status:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>extype <select name="extype" id="extypethread" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',extype:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function referralSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typereferral" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function publicationSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typepublication" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Internal">Internal</a>
					<option value=""></a>
					<option value="Book">Book</a>
					<option value="Proceedings">Proceedings</a>
					<option value="Research">Research</a>
					<option value="Funding">Funding</a>
					<option value="Patent">Patent</a>
					<option value="Magazine">Magazine</a>
					<option value="Newspaper">Newspaper</a>
					<option value="Journal">Journal</a>
							</select></p>
				<p>category <select name="category" id="categorypublication" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Column">Column</a>
					<option value=""></a>
					<option value="Grant">Grant</a>
					<option value="Article">Article</a>
					<option value="Application">Application</a>
					<option value="Chapter">Chapter</a>
					<option value="Report">Report</a>
							</select></p>
				<p>catdetails <select name="catdetails" id="catdetailspublication" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',catdetails:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Refereed">Refereed</a>
					<option value=" "> </a>
					<option value="Unrefereed">Unrefereed</a>
							</select></p>
		</div>`;
	};

	
	function productSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typeproduct" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="environment">Environment</a>
					<option value="Network">Network</a>
					<option value="platform">Platform</a>
					<option value="thing">Thing</a>
					<option value="cots">Commercial Software</a>
					<option value="Language">Language</a>
					<option value="hardware">Hardware</a>
					<option value="documentation">Documentation</a>
					<option value="service">Service</a>
					<option value="open source">Open Source Software</a>
					<option value="Open Content">Open Content</a>
					<option value="app">App</a>
							</select></p>
				<p>category <select name="category" id="categoryproduct" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Team">Team</a>
					<option value="Student">Student</a>
					<option value="Game">Game</a>
					<option value="Identity">Identity</a>
					<option value="SEO">SEO</a>
					<option value="Learning Design">Learning Design</a>
					<option value="security">Security</a>
					<option value="School">School</a>
					<option value="eMail">eMail</a>
					<option value="Computer">Computer</a>
					<option value="Note">Note</a>
					<option value="performance">Performance</a>
					<option value="Prototype">Prototype</a>
					<option value="Payment">Payment</a>
					<option value="newsletter">Newsletter</a>
					<option value="Animation">Animation</a>
					<option value="Class">Class</a>
					<option value="eBook">eBook</a>
					<option value="Learning Content">Learning Content</a>
					<option value="VR">VR</a>
					<option value="Test">Test</a>
					<option value="Blog">Blog</a>
					<option value="Form">Form</a>
					<option value="Database">Database</a>
					<option value="Image">Image</a>
					<option value="Photo">Photo</a>
					<option value="Discussion">Discussion</a>
					<option value="Quiz">Quiz</a>
					<option value="Survey">Survey</a>
					<option value="Project">Project</a>
					<option value="Content">Content</a>
					<option value="Video">Video</a>
					<option value="Lecture">Lecture</a>
					<option value="Metadata">Metadata</a>
					<option value="Employment">Employment</a>
					<option value="Text">Text</a>
					<option value="Citation">Citation</a>
					<option value="voice">Voice</a>
					<option value="Screen">Screen</a>
					<option value="Website">Website</a>
					<option value="Workforce">Workforce</a>
					<option value="File">File</a>
					<option value="Course">Course</a>
					<option value="Presentation">Presentation</a>
					<option value="Comment">Comment</a>
					<option value="Portfolio">Portfolio</a>
					<option value="artificial intelligence">Artificial intelligence</a>
					<option value="Learning">Learning</a>
					<option value="Spreadsheet">Spreadsheet</a>
					<option value="Journal">Journal</a>
					<option value="Social">Social</a>
					<option value="Research">Research</a>
					<option value="Learning Object">Learning Object</a>
					<option value="Competency">Competency</a>
					<option value="ai">Ai</a>
					<option value="Message">Message</a>
					<option value="Simulation">Simulation</a>
					<option value="Event">Event</a>
					<option value="virtualization">Virtualization</a>
					<option value="Microcontent">Microcontent</a>
					<option value="AR">AR</a>
					<option value="3D">3D</a>
					<option value="Software">Software</a>
					<option value="Feed/API">Feed/API</a>
					<option value="Advertising">Advertising</a>
					<option value="Audio">Audio</a>
							</select></p>
				<p>genre <select name="genre" id="genreproduct" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',genre:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="Server">Server</a>
					<option value="Robotics">Robotics</a>
					<option value="Management">Management</a>
					<option value="Authoring">Authoring</a>
					<option value="Platform">Platform</a>
					<option value="conferencing">Conferencing</a>
					<option value="authentication">Authentication</a>
					<option value="evaluation">Evaluation</a>
					<option value="Library">Library</a>
					<option value="Amplification">Amplification</a>
					<option value="Validation">Validation</a>
					<option value="Gaming">Gaming</a>
					<option value="streaming">Streaming</a>
					<option value="Discovery">Discovery</a>
					<option value="Hosting">Hosting</a>
					<option value="Monitoring">Monitoring</a>
					<option value="Viewer">Viewer</a>
					<option value="Environment">Environment</a>
					<option value="Network">Network</a>
					<option value="Communication">Communication</a>
					<option value="Assistant">Assistant</a>
					<option value="Calendar">Calendar</a>
					<option value="deployment">Deployment</a>
					<option value="Capture">Capture</a>
					<option value="Analytics">Analytics</a>
					<option value="Webcasting">Webcasting</a>
					<option value="Charging">Charging</a>
					<option value="support">Support</a>
					<option value="Converting">Converting</a>
					<option value="Browser">Browser</a>
					<option value="Captioning">Captioning</a>
					<option value="Production">Production</a>
					<option value="Repository">Repository</a>
					<option value="Curation">Curation</a>
					<option value="Framework">Framework</a>
					<option value="programming">Programming</a>
					<option value="Community">Community</a>
					<option value="Delivery">Delivery</a>
					<option value="Design">Design</a>
					<option value="Marketplace">Marketplace</a>
					<option value="Printing">Printing</a>
					<option value="Integration">Integration</a>
					<option value="Exchange">Exchange</a>
					<option value="Display">Display</a>
					<option value="Publishing">Publishing</a>
					<option value="Editing">Editing</a>
					<option value="Language">Language</a>
					<option value="Registry">Registry</a>
					<option value="Collaboration">Collaboration</a>
					<option value="Annotation">Annotation</a>
					<option value="Aggregating">Aggregating</a>
							</select></p>
		</div>`;
	};

	
	function configSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>type <select name="type" id="typeconfig" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function graphSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>typeval <select name="typeval" id="typevalgraph" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',typeval:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
				<p>type <select name="type" id="typegraph" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',type:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="something else">something</a>
							</select></p>
		</div>`;
	};

	
	function institutionSearchTemplate(request) {	
		return `<button class="accordion" onClick="togglePanel(this.nextElementSibling);">Filter ${request.table}</button>
		<div class="panel">
		
				<p>category <select name="category" id="categoryinstitution" 
				onChange="alert(this.value);loadList({div:'${request.div}',cmd:'${request.cmd}',table:'${request.table}',category:this.value});">
				    <option value="all" selected>All</a>
			
					<option value="university">University</a>
					<option value="centre">Centre</a>
					<option value="school">School</a>
					<option value="museum">Museum</a>
					<option value="school board">School board</a>
					<option value="college">College</a>
					<option value="government">Government</a>
					<option value="nonprofit">Nonprofit</a>
							</select></p>
		</div>`;
	};

	