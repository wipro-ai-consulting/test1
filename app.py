<!DOCTYPE html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta
			name="viewport"
			content="width=device-width, initial-scale=1.0, user-scalable=no"
		/>
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta property="og:title" content="app.py · merve/write-with-transformer at main" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/spaces/merve/write-with-transformer/blob/main/app.py" />
		<meta property="og:image" content="https://huggingface.co/front/thumbnails/v2-2.png" />

		<link rel="stylesheet" href="/front/build/style.c4dc3d96.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>
		<link
			rel="stylesheet"
			href="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.css"
		/>

		 

		<title>app.py · merve/write-with-transformer at main</title>
	</head>
	<body
		class="flex flex-col min-h-screen bg-white dark:bg-gray-950 text-black ViewerBlobPage"
	>
		<div class="flex flex-col min-h-screen "><header class="border-b border-gray-100"><div class="w-full px-4 lg:px-6 xl:container flex items-center h-16"><div class="flex flex-1 items-center"><a class="flex flex-none items-center mr-5 lg:mr-6" href="/"><img alt="Hugging Face's logo" class="md:mr-2 w-7" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden text-lg font-bold whitespace-nowrap md:block">Hugging Face</span></a>
			<div class="SVELTE_HYDRATER flex-1 lg:max-w-sm mr-2 sm:mr-4 lg:mr-6" data-props="{&quot;header&quot;:true,&quot;placeholder&quot;:&quot;Search models, datasets, users...&quot;,&quot;url&quot;:&quot;/api/quicksearch&quot;,&quot;searchParams&quot;:{&quot;withLinks&quot;:true}}" data-target="QuickSearch"><div class="relative "><input autocomplete="off" class="w-full dark:bg-gray-950 
			form-input-alt h-9 pl-8 pr-3 focus:shadow-xl" name="" placeholder="Search models, datasets, users..."  spellcheck="false" type="text">
	<svg class="absolute left-2.5 top-2.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div></div>
			<div class="SVELTE_HYDRATER " data-props="{&quot;apiInferenceUrl&quot;:&quot;https://api-inference.huggingface.co&quot;}" data-target="NavigationMenuPhone"><button class="lg:hidden relative flex-none place-self-stretch flex items-center justify-center w-8" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="22" height="22" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M4 24h24v2H4z"></path><path d="M4 12h24v2H4z"></path><path d="M4 18h24v2H4z"></path><path d="M4 6h24v2H4z"></path></svg></button>
</div></div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center space-x-2"><li><a class="flex items-center group px-2 py-0.5 hover:text-indigo-700 dark:hover:text-gray-400" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
				Models
			</a></li>
		<li><a class="flex items-center group px-2 py-0.5 hover:text-red-700 dark:hover:text-gray-400" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
				Datasets
			</a></li>
		<li><a class="flex items-center group px-2 py-0.5 hover:text-blue-700 dark:hover:text-blue-400" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
				Spaces
			</a></li>
		<li><a class="flex items-center group px-2 py-0.5 hover:text-yellow-700 dark:hover:text-yellow-400" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path opacity="0.5" d="M20.9022 5.10334L10.8012 10.8791L7.76318 9.11193C8.07741 8.56791 8.5256 8.11332 9.06512 7.7914L15.9336 3.73907C17.0868 3.08811 18.5002 3.26422 19.6534 3.91519L19.3859 3.73911C19.9253 4.06087 20.5879 4.56025 20.9022 5.10334Z" fill="currentColor"></path><path d="M10.7999 10.8792V28.5483C10.2136 28.5475 9.63494 28.4139 9.10745 28.1578C8.5429 27.8312 8.074 27.3621 7.74761 26.7975C7.42122 26.2327 7.24878 25.5923 7.24756 24.9402V10.9908C7.25062 10.3319 7.42358 9.68487 7.74973 9.1123L10.7999 10.8792Z" fill="currentColor" fill-opacity="0.75"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M21.3368 10.8499V6.918C21.3331 6.25959 21.16 5.61234 20.8346 5.03949L10.7971 10.8727L10.8046 10.874L21.3368 10.8499Z" fill="currentColor"></path><path opacity="0.5" d="M21.7937 10.8488L10.7825 10.8741V28.5486L21.7937 28.5234C23.3344 28.5234 24.5835 27.2743 24.5835 25.7335V13.6387C24.5835 12.0979 23.4365 11.1233 21.7937 10.8488Z" fill="currentColor"></path></svg>
				Docs
			</a></li>

		<li><div class="relative  v2-dropdown">
	<button class="
			px-2 py-0.5 group hover:text-green-700 dark:hover:text-gray-400 flex items-center
			
			v2-dropdown-button" type="button">
		<svg class="mr-1.5 text-gray-400 group-hover:text-green-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M19 6H5a3 3 0 0 0-3 3v2.72L8.837 14h6.326L22 11.72V9a3 3 0 0 0-3-3z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M10 6V5h4v1h2V5a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v1h2zm-1.163 8L2 11.72V18a3.003 3.003 0 0 0 3 3h14a3.003 3.003 0 0 0 3-3v-6.28L15.163 14H8.837z" fill="currentColor"></path></svg>
			Solutions
			</button>
	
	
	<div class="absolute top-full mt-1 min-w-full w-auto bg-white rounded-xl overflow-hidden shadow-lg z-10 border border-gray-100
		left-0
		!w-64 !mt-2 v2-dropdown-menu hidden"><ul class="min-w-full w-auto">
					<li><ul><li><a href="/support" data-ga-category="header-menu" data-ga-action="clicked support" data-ga-label="premium support" class="flex items-center group hover:bg-gradient-to-r hover:from-gray-100 p-2 w-80 dark:hover:from-gray-800"><div class="h-9 w-9 bg-gradient-to-tr dark:bg-gray-800 bg-gray-100 group-hover:bg-white dark:group-hover:bg-black rounded mr-1.5 flex items-center justify-center flex-none"><svg class="text-lg text-gray-500 group-hover:text-gray-600 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 24"><path d="M12.6213 22.4475C12.7096 22.4825 12.8038 22.5003 12.8988 22.5C13.068 22.4991 13.2318 22.4409 13.3638 22.335L17.1138 19.335C17.2022 19.2652 17.2737 19.1763 17.323 19.0751C17.3724 18.9738 17.3983 18.8627 17.3988 18.75V13.0575L20.2338 10.23C21.0025 9.46567 21.6117 8.5563 22.0263 7.55467C22.4409 6.55304 22.6524 5.47907 22.6488 4.39505V3.00005C22.6488 2.60222 22.4908 2.22069 22.2095 1.93939C21.9281 1.65808 21.5466 1.50005 21.1488 1.50005H19.7538C18.6698 1.49639 17.5958 1.70798 16.5942 2.12254C15.5925 2.5371 14.6832 3.14638 13.9188 3.91505L11.0913 6.75005H5.39879C5.28552 6.75146 5.17405 6.77851 5.07273 6.82917C4.97141 6.87983 4.88288 6.95278 4.81379 7.04255L1.81379 10.7925C1.73008 10.8963 1.67553 11.0205 1.65576 11.1523C1.63599 11.2841 1.6517 11.4188 1.70129 11.5425C1.75027 11.6654 1.83088 11.7732 1.93494 11.8548C2.03899 11.9365 2.1628 11.9892 2.29379 12.0075L7.54379 12.7575L11.4063 16.605L12.1563 21.855C12.1747 21.986 12.2274 22.1098 12.309 22.2139C12.3907 22.318 12.4984 22.3986 12.6213 22.4475Z" opacity=".5" fill="currentColor"></path><path d="M11.0837 10.9416L5.08569 16.9396L7.20363 19.0576L13.2017 13.0595L11.0837 10.9416Z" opacity="1" fill="currentColor"></path></svg></div>
										<div class="font-medium leading-tight">Expert Support
											<p class="text-sm font-normal text-gray-400 whitespace-nowrap">Accelerate your ML roadmap</p>
										</div></a>
								</li><li><a href="/inference-api" data-ga-category="header-menu" data-ga-action="clicked inference api" data-ga-label="accelerated inference" class="flex items-center group hover:bg-gradient-to-r hover:from-gray-100 p-2 w-80 dark:hover:from-gray-800"><div class="h-9 w-9 bg-gradient-to-tr dark:bg-gray-800 bg-gray-100 group-hover:bg-white dark:group-hover:bg-black rounded mr-1.5 flex items-center justify-center flex-none"><svg class="text-lg text-gray-500 group-hover:text-gray-600 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M8 9H4a2 2 0 0 0-2 2v12h2v-5h4v5h2V11a2 2 0 0 0-2-2zm-4 7v-5h4v5z" fill="currentColor"></path><path d="M22 11h3v10h-3v2h8v-2h-3V11h3V9h-8v2z" fill="currentColor"></path><path d="M14 23h-2V9h6a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-4zm0-7h4v-5h-4z" fill="currentColor"></path></svg></div>
										<div class="font-medium leading-tight">Inference API
											<p class="text-sm font-normal text-gray-400 whitespace-nowrap">Use +20k models via API calls</p>
										</div></a>
								</li><li><a href="/autonlp" data-ga-category="header-menu" data-ga-action="clicked autonlp" data-ga-label="autonlp" class="flex items-center group hover:bg-gradient-to-r hover:from-gray-100 p-2 w-80 dark:hover:from-gray-800"><div class="h-9 w-9 bg-gradient-to-tr dark:bg-gray-800 bg-gray-100 group-hover:bg-white dark:group-hover:bg-black rounded mr-1.5 flex items-center justify-center flex-none"><svg class="text-lg text-gray-500 group-hover:text-gray-600 dark:group-hover:text-gray-400" viewBox="0 0 327 270" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" style="transform: rotate(360deg);"><path fill-rule="evenodd" clip-rule="evenodd" d="M51.963 85.696L51.9843 85.7142L52.0059 85.732C55.1982 88.3543 59.2834 89.5397 63.9988 89.5397H78.4986V69.3054H70.5681V40.5348C70.5681 30.8859 67.5907 23.2435 61.2359 18.1491C55.13 13.0873 46.7983 10.7302 36.5895 10.7302C28.2498 10.7302 21.1616 12.1163 15.4724 15.0602C10.0168 17.8391 5.83986 21.4966 3.12193 26.0961L2.00182 27.9917L17.1258 41.4352L18.8589 39.0419C20.6131 36.6193 22.6796 34.6836 25.06 33.2061C27.1956 31.8806 30.1823 31.1037 34.2242 31.1037C38.6379 31.1037 41.027 32.1553 42.2298 33.5299L42.2688 33.5745L42.3098 33.6174C43.6986 35.0693 44.6292 37.486 44.6292 41.3696V42.3135H35.7547C24.9484 42.3135 16.3129 44.149 10.2104 48.1829C3.87027 52.3738 0.802246 58.8507 0.802246 67.1092C0.802246 74.4698 3.09622 80.537 7.93618 84.9467L7.95908 84.9676L7.98247 84.9879C12.8409 89.2126 19.125 91.2093 26.5719 91.2093C32.519 91.2093 37.7242 89.9194 42.0438 87.1839C44.6415 85.5735 46.7327 83.5117 48.3183 81.0336C49.2175 82.8133 50.4256 84.3783 51.963 85.696ZM49.1349 74.4024C49.1268 74.3369 49.119 74.2711 49.1115 74.205C49.1158 74.2426 49.1201 74.2801 49.1246 74.3175C49.128 74.3458 49.1314 74.3741 49.1349 74.4024ZM42.0076 70.2099C40.0307 71.601 37.5325 72.3663 34.3634 72.3663C31.4475 72.3663 29.4241 71.7802 28.0549 70.8674C26.9105 70.1045 26.3237 69.0722 26.3237 67.3875V64.6048C26.3237 62.5484 27.028 61.3156 28.304 60.4603C29.7696 59.4779 32.3054 58.7913 36.3112 58.7913H44.6292V64.744C44.6292 67.3052 43.7283 68.999 42.0076 70.2099ZM101.033 89.3317L101.067 89.346L101.102 89.3594C104.318 90.6044 107.803 91.2093 111.528 91.2093C117.713 91.2093 122.939 89.6592 126.894 86.2606C128.359 85.0311 129.675 83.697 130.838 82.2601V89.5397H156.776V12.3998H130.838V62.2396C130.838 63.6201 130.55 64.6767 130.077 65.5045C129.516 66.4857 128.783 67.3276 127.859 68.041C127.056 68.6406 126.032 69.1518 124.739 69.5376C123.49 69.8452 122.196 70.001 120.85 70.001C117.332 70.001 115.151 69.0073 113.789 67.4414C112.364 65.8044 111.419 63.0712 111.419 58.7612V12.3998H85.4801V61.5439C85.4801 66.125 86.0642 70.2695 87.2869 73.9374L87.2973 73.9689L87.3086 74C88.6115 77.608 90.3932 80.7401 92.6858 83.3453C94.9963 85.9709 97.7881 87.9709 101.033 89.3317ZM166.262 12.3998V33.7473H185.741V66.1353C185.741 72.7418 187.742 78.3845 191.881 82.8418C196.179 87.4702 202.536 89.5397 210.397 89.5397H239.645V68.1923H211.68V33.7473H239.645V12.3998H211.68V0.359375H187.41V6.58626C187.41 9.65572 186.762 10.8926 186.317 11.3055C185.766 11.8168 184.435 12.3998 181.597 12.3998H166.262ZM272.247 88.5173L272.27 88.5262L272.293 88.5347C277.091 90.3342 282.425 91.2093 288.258 91.2093C294.09 91.2093 299.424 90.3342 304.223 88.5347L304.246 88.5262L304.268 88.5173C309.051 86.6239 313.139 83.9115 316.486 80.3663C319.921 76.8262 322.52 72.5541 324.304 67.5974C326.096 62.6209 326.967 57.0662 326.967 50.9698C326.967 44.8733 326.096 39.3187 324.304 34.3421C322.52 29.3855 319.921 25.1134 316.486 21.5733C313.135 18.0231 309.038 15.3534 304.246 13.5525C299.439 11.6538 294.097 10.7302 288.258 10.7302C282.418 10.7302 277.076 11.6538 272.27 13.5525C267.477 15.3534 263.342 18.0202 259.905 21.5585L259.891 21.5728L259.877 21.5873C256.539 25.1276 253.992 29.3954 252.211 34.3421C250.42 39.3187 249.549 44.8733 249.549 50.9698C249.549 57.0662 250.42 62.6209 252.211 67.5974C253.992 72.5442 256.539 76.812 259.877 80.3523L259.891 80.3668L259.905 80.3811C263.337 83.9145 267.464 86.6239 272.247 88.5173ZM297.126 67.1259C295.135 69.3301 292.301 70.5576 288.258 70.5576C284.214 70.5576 281.38 69.3301 279.389 67.1259C277.376 64.8968 276.183 61.5428 276.183 56.6742V45.2653C276.183 40.3968 277.376 37.0428 279.389 34.8136C281.38 32.6095 284.214 31.382 288.258 31.382C292.301 31.382 295.135 32.6095 297.126 34.8136C299.14 37.0428 300.332 40.3968 300.332 45.2653V56.6742C300.332 61.5428 299.14 64.8968 297.126 67.1259Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M24.1832 151.837C24.1832 149.255 26.2767 147.161 28.8594 147.161H73.3409C73.3027 147.546 73.2833 147.936 73.2833 148.33V185.74C73.2833 192.196 78.5171 197.43 84.9737 197.43C91.4303 197.43 96.6642 192.196 96.6642 185.74V148.33C96.6642 147.936 96.6448 147.546 96.6066 147.161H117.511C116.885 148.593 116.538 150.175 116.538 151.837V246.53H65.0999V202.107C65.0999 195.65 59.866 190.416 53.4094 190.416C46.9528 190.416 41.7189 195.65 41.7189 202.107V246.53H28.8594C26.2767 246.53 24.1832 244.437 24.1832 241.854V151.837ZM139.919 246.53H234.873C234.702 245.778 234.612 244.996 234.612 244.192C234.612 238.381 229.901 233.671 224.091 233.671H193.695C183.365 233.671 174.99 225.296 174.99 214.966V147.161H138.946C139.572 148.593 139.919 150.175 139.919 151.837V246.53ZM298.91 246.53H257.458C257.805 245.423 257.993 244.245 257.993 243.023V228.995C257.993 218.664 249.619 210.29 239.288 210.29H217.076C206.746 210.29 198.371 201.915 198.371 191.585V147.161H298.91C301.492 147.161 303.586 149.255 303.586 151.837V241.854C303.586 244.437 301.492 246.53 298.91 246.53ZM28.8594 123.78C13.3638 123.78 0.802246 136.342 0.802246 151.837V241.854C0.802246 257.35 13.3638 269.911 28.8594 269.911H298.91C314.405 269.911 326.967 257.35 326.967 241.854V151.837C326.967 136.342 314.405 123.78 298.91 123.78H28.8594ZM240.457 162.359C231.418 162.359 224.091 169.686 224.091 178.726C224.091 187.765 231.418 195.092 240.457 195.092C249.496 195.092 256.824 187.765 256.824 178.726C256.824 169.686 249.496 162.359 240.457 162.359Z" fill="currentColor"></path></svg></div>
										<div class="font-medium leading-tight">AutoNLP
											<p class="text-sm font-normal text-gray-400 whitespace-nowrap">Create ML models without code</p>
										</div></a>
								</li><li><a href="/infinity" data-ga-category="header-menu" data-ga-action="clicked infinity" data-ga-label="infinity" class="flex items-center group hover:bg-gradient-to-r hover:from-gray-100 p-2 w-80 dark:hover:from-gray-800"><div class="h-9 w-9 bg-gradient-to-tr dark:bg-gray-800 bg-gray-100 group-hover:bg-white dark:group-hover:bg-black rounded mr-1.5 flex items-center justify-center flex-none"><svg class="text-lg text-gray-500 group-hover:text-gray-600 dark:group-hover:text-gray-400" width="1em" height="1em" viewBox="0 0 349 155" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M77.4254 42.0939C58.0156 42.0939 42.2809 57.799 42.2809 77.1722C42.2809 96.5454 58.0156 112.25 77.4254 112.25V154.344C34.7239 154.344 0.107422 119.793 0.107422 77.1722C0.107422 34.5512 34.7239 0 77.4254 0C116.684 0 144.788 19.3459 167.187 40.3015L137.675 70.504C118.96 53.1048 101.389 42.0939 77.4254 42.0939ZM181.033 114.057C203.574 135.043 231.897 154.344 271.531 154.344V112.25C247.156 112.25 229.306 101.201 210.542 83.8571L181.033 114.057Z" fill="currentColor" opacity="0.5"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M271.141 42.0939C290.551 42.0939 306.286 57.799 306.286 77.1722C306.286 96.5454 290.551 112.25 271.141 112.25V112.304C270.876 112.294 270.609 112.289 270.34 112.289C258.72 112.289 249.3 121.709 249.3 133.329C249.3 144.949 258.72 154.369 270.34 154.369C270.685 154.369 271.027 154.36 271.368 154.344C313.965 154.222 348.459 119.718 348.459 77.1722C348.459 34.5512 313.843 0 271.141 0C219.197 0 186.78 33.8682 161.269 60.5213C160.594 61.227 159.923 61.9276 159.257 62.6224C131.402 91.6825 110.291 112.25 77.0352 112.25V112.289C77.0352 112.289 77.0352 112.289 77.0351 112.289C65.4151 112.289 55.9951 121.709 55.9951 133.329C55.9951 144.949 65.4151 154.369 77.0351 154.369C77.4121 154.369 77.7867 154.359 78.1587 154.339C130.221 153.858 162.646 120.001 188.168 93.3526L188.213 93.306L188.262 93.255C188.754 92.7412 189.243 92.2301 189.73 91.722C217.708 62.5338 238.492 42.0939 271.141 42.0939Z" fill="currentColor"></path></svg></div>
										<div class="font-medium leading-tight">Infinity
											<p class="text-sm font-normal text-gray-400 whitespace-nowrap">Optimize to 1ms latency</p>
										</div></a>
								</li><li><a href="/hardware" data-ga-category="header-menu" data-ga-action="clicked hardware" data-ga-label="hardware" class="flex items-center group hover:bg-gradient-to-r hover:from-gray-100 p-2 w-80 dark:hover:from-gray-800"><div class="h-9 w-9 bg-gradient-to-tr dark:bg-gray-800 bg-gray-100 group-hover:bg-white dark:group-hover:bg-black rounded mr-1.5 flex items-center justify-center flex-none"><svg class="text-lg text-gray-500 group-hover:text-gray-600 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 230 230"><path fill-rule="evenodd" clip-rule="evenodd" d="M196.384 70.1626V77.0991C196.378 80.4596 195.489 83.7596 193.808 86.6691C192.126 89.5785 189.71 91.9955 186.801 93.6783L123.359 130.287C120.724 131.532 117.839 132.184 114.926 132.203V106.1L193.797 60.4834C195.474 63.4351 196.365 66.7701 196.384 70.1626ZM196.384 111.562V118.499C196.378 121.859 195.489 125.159 193.808 128.068C192.126 130.978 189.71 133.395 186.801 135.078L123.359 171.686C120.724 172.932 117.839 173.584 114.926 173.603V147.499L193.797 101.883C195.474 104.834 196.365 108.169 196.384 111.562ZM196.384 159.897V152.96C196.365 149.568 195.474 146.233 193.797 143.281L114.926 188.898V215.001C117.839 214.982 120.724 214.33 123.359 213.084L186.801 176.476C189.71 174.793 192.126 172.376 193.808 169.467C195.489 166.557 196.378 163.257 196.384 159.897Z" fill="currentColor"></path><path opacity="0.25" fill-rule="evenodd" clip-rule="evenodd" d="M193.605 60.4489L160.32 79.7003L186.897 95.0442C189.676 96.7021 191.985 99.05 193.605 101.848L160.32 121.099L186.897 136.443C189.676 138.101 191.985 140.448 193.605 143.247L114.734 188.863L35.8633 143.247C37.4824 140.444 39.7917 138.101 42.5716 136.443L44.3827 135.397L106.355 171.226C109.073 172.546 112.054 173.234 115.075 173.239V147.499L36.2047 101.883C36.1814 101.924 36.1583 101.965 36.1353 102.006L35.8633 101.848C37.4824 99.0452 39.7917 96.7029 42.5716 95.0442L44.3836 93.9981L106.355 129.827C109.073 131.147 112.054 131.835 115.075 131.839V106.1L36.2047 60.4834C36.1814 60.5243 36.1583 60.5652 36.1353 60.6063L35.8633 60.4489C37.4824 57.6458 39.7917 55.3035 42.5716 53.6448L105.151 17.5156C111.092 14.1615 118.376 14.1615 124.317 17.5156L186.897 53.6448C189.676 55.3027 191.985 57.6506 193.605 60.4489Z" fill="currentColor"></path><path opacity="0.5" fill-rule="evenodd" clip-rule="evenodd" d="M115.075 131.435V105.696L36.2047 60.0791C34.5242 63.0293 33.633 66.3631 33.6172 69.7583V76.3307C33.6235 79.6912 34.512 82.9912 36.1938 85.9006C37.8755 88.8101 40.2917 91.227 43.2005 92.9098L106.355 129.422C109.073 130.742 112.054 131.43 115.075 131.435ZM115.075 147.499V173.239C112.054 173.234 109.073 172.546 106.355 171.226L43.2005 134.714C40.2917 133.031 37.8755 130.614 36.1938 127.704C34.512 124.795 33.6235 121.495 33.6172 118.134V111.562C33.633 108.167 34.5242 104.833 36.2047 101.883L115.075 147.499ZM115.075 188.898V214.637C112.054 214.633 109.073 213.945 106.355 212.624L43.2005 176.112C40.2917 174.429 37.8755 172.012 36.1938 169.103C34.512 166.193 33.6235 162.893 33.6172 159.533V152.96C33.633 149.565 34.5242 146.231 36.2047 143.281L115.075 188.898Z" fill="currentColor"></path></svg></div>
										<div class="font-medium leading-tight">Hardware
											<p class="text-sm font-normal text-gray-400 whitespace-nowrap">Scale with dedicated hardware</p>
										</div></a>
								</li><li><a href="/platform" data-ga-category="header-menu" data-ga-action="clicked platform" data-ga-label="platform" class="flex items-center group hover:bg-gradient-to-r hover:from-gray-100 p-2 w-80 dark:hover:from-gray-800"><div class="h-9 w-9 bg-gradient-to-tr dark:bg-gray-800 bg-gray-100 group-hover:bg-white dark:group-hover:bg-black rounded mr-1.5 flex items-center justify-center flex-none"><svg class="text-lg text-gray-500 group-hover:text-gray-600 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg></div>
										<div class="font-medium leading-tight">Platform
											<p class="text-sm font-normal text-gray-400 whitespace-nowrap">Collaborate better on ML</p>
										</div></a>
								</li></ul></li>
				</ul></div>
	</div></li>

		<li><a class="flex items-center group px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/pricing" data-ga-category="header-menu" data-ga-action="clicked pricing" data-ga-label="pricing">Pricing
			</a></li>
		<li><div class="relative group v2-dropdown">
	<button class="
			px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center
			
			v2-dropdown-button" type="button">
		<svg class="mr-1.5 text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
			</button>
	
	
	<div class="absolute top-full mt-1 min-w-full w-auto bg-white rounded-xl overflow-hidden shadow-lg z-10 border border-gray-100
		right-0
		!w-52 !mt-3 v2-dropdown-menu hidden"><ul class="min-w-full w-auto">
					<li><div class="col-span-full px-4 py-0.5 flex items-center justify-between font-semibold bg-gradient-to-r to-white dark:to-gray-925 whitespace-nowrap text-blue-800 from-blue-50 dark:text-blue-100 dark:from-blue-900">Website
						</div>
						<ul><li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			hover:underline
			v2-dropdown-entry" href="/tasks">
		<svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M15.273 18.728A6.728 6.728 0 1 1 22 11.999V12a6.735 6.735 0 0 1-6.727 6.728z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M8.727 18.728A6.728 6.728 0 1 1 15.455 12a6.735 6.735 0 0 1-6.728 6.728z" fill="currentColor"></path></svg>
			Tasks</a></li>

							<li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			hover:underline
			v2-dropdown-entry" href="/metrics">
		<svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M6 23H2a1 1 0 0 1-1-1v-8a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1z" opacity=".25" fill="currentColor"></path><path class="uim-primary" d="M14 23h-4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v20a1 1 0 0 1-1 1z" fill="currentColor"></path><path class="uim-tertiary" d="M22 23h-4a1 1 0 0 1-1-1V10a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1z" opacity=".5" fill="currentColor"></path></svg>
			Metrics</a></li>

							<li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			hover:underline
			v2-dropdown-entry" href="/languages">
		<svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-primary" d="M17 13H7a1 1 0 0 1 0-2h10a1 1 0 0 1 0 2z" fill="currentColor"></path><path class="uim-tertiary" d="M12 2a10 10 0 0 0-7.743 16.33l-1.964 1.963A1 1 0 0 0 3 22h9a10 10 0 0 0 0-20zM9 7h6a1 1 0 0 1 0 2H9a1 1 0 0 1 0-2zm6 10H9a1 1 0 0 1 0-2h6a1 1 0 0 1 0 2zm2-4H7a1 1 0 0 1 0-2h10a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M15 17H9a1 1 0 0 1 0-2h6a1 1 0 0 1 0 2zm0-8H9a1 1 0 0 1 0-2h6a1 1 0 0 1 0 2z" fill="currentColor"></path></svg>
			Languages</a></li>
							<li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			hover:underline
			v2-dropdown-entry" href="/organizations">
		<svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M12 18a3.5 3.5 0 1 1 3.5-3.5A3.504 3.504 0 0 1 12 18z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M14.64 16.772a3.452 3.452 0 0 1-5.28 0A4.988 4.988 0 0 0 7 21a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1a4.988 4.988 0 0 0-2.36-4.228z" fill="currentColor"></path><path class="uim-tertiary" d="M21 12a.996.996 0 0 1-.664-.252L12 4.338l-8.336 7.41a1 1 0 0 1-1.328-1.496l9-8a.999.999 0 0 1 1.328 0l9 8A1 1 0 0 1 21 12z" opacity=".5" fill="currentColor"></path><path class="uim-quaternary" d="M12 4.338l-8 7.111V21a1 1 0 0 0 1 1h3a1 1 0 0 1-1-1a4.988 4.988 0 0 1 2.36-4.228A3.469 3.469 0 0 1 8.5 14.5a3.5 3.5 0 0 1 7 0a3.469 3.469 0 0 1-.86 2.272A4.988 4.988 0 0 1 17 21a1 1 0 0 1-1 1h3a1 1 0 0 0 1-1v-9.551z" opacity=".25" fill="currentColor"></path></svg>
			Organizations</a></li></ul></li>
					<li><div class="col-span-full px-4 py-0.5 flex items-center justify-between font-semibold bg-gradient-to-r to-white dark:to-gray-925 whitespace-nowrap text-yellow-800 from-yellow-50 dark:text-yellow-100 dark:from-yellow-900">Community
						</div>
						<ul><li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			hover:underline
			v2-dropdown-entry" href="/course">
		<svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 32"><path fill-rule="evenodd" clip-rule="evenodd" d="M5.44971 14.5964L5.44977 19.5221L5.44971 19.5321L5.44977 19.5422V19.6062H5.4533C5.59676 21.0844 10.0242 22.2706 15.465 22.2706C20.9057 22.2706 25.3332 21.0844 25.4767 19.6062H25.4803L25.4802 14.8524L15.7373 17.5754L5.44971 14.5964Z" fill="currentColor" fill-opacity="0.8"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.16846 11.7412L15.7374 15.9487L30.832 11.7412V13.3494H30.8069L30.832 13.3566L15.7374 17.5754L1.16846 13.3566L1.1927 13.3494H1.16846V11.7412ZM1.16846 11.7412V11.7412L1.16849 11.7412L1.16846 11.7412ZM1.16846 11.7412V11.6674H1.41519L1.16846 11.7412ZM30.5764 11.6674H30.832V11.7412L30.5764 11.6674Z" fill="currentColor" fill-opacity="0.5"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M3.02827 18.7976C3.398 17.0129 4.40214 15.3593 5.21357 14.3777L5.68497 14.7674C4.91639 15.6971 3.97099 17.2621 3.62717 18.9216C3.28615 20.5676 3.53867 22.2742 5.1103 23.5887C5.88204 24.2342 6.92784 24.5392 8.1691 24.6236C9.40985 24.7079 10.8132 24.5697 12.2706 24.3583C12.9462 24.2603 13.6292 24.1473 14.3104 24.0346C14.3626 24.0259 14.4148 24.0173 14.467 24.0087C15.1987 23.8877 15.9275 23.7684 16.6346 23.6714C18.0439 23.4782 19.3924 23.3696 20.5369 23.5201L20.4572 24.1265C19.3982 23.9872 18.1177 24.0854 16.7176 24.2774C16.0201 24.373 15.2991 24.491 14.5667 24.6121C14.5143 24.6208 14.4618 24.6295 14.4093 24.6382C13.7292 24.7507 13.0404 24.8647 12.3583 24.9636C10.8913 25.1764 9.43547 25.3227 8.12763 25.2338C6.8203 25.145 5.62813 24.8191 4.71791 24.0579C2.92563 22.5589 2.65573 20.5957 3.02827 18.7976Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M20.4304 24.1128L20.5291 23.5358L28.0463 24.2759L27.9888 24.8599L27.966 24.8577L27.8807 25.3377L27.8992 25.3422L27.7593 25.9121L20.4304 24.1128Z" fill="currentColor" fill-opacity="0.25"></path><path d="M15.7374 15.9487L1.16846 11.7412L15.7374 7.38605L30.832 11.7412L15.7374 15.9487Z" fill="currentColor" fill-opacity="0.25"></path></svg>
			Course</a></li>
							<li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			hover:underline
			v2-dropdown-entry" href="/blog">
		<svg class="mr-1.5 text-gray-300 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M10 4H4c-1.11 0-2 .89-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-8l-2-2z" fill="currentColor"></path></svg>
			Blog</a></li>
							<li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			hover:underline
			v2-dropdown-entry" href="/join/discord" target="_blank">
		<svg class="mr-1.5 text-gray-300 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 32" preserveAspectRatio="xMidYMid meet"><path d="M25.6933 7.10665C23.92 6.27998 22 5.67998 20 5.33331C19.9825 5.33275 19.965 5.33604 19.9489 5.34295C19.9328 5.34987 19.9183 5.36023 19.9067 5.37331C19.6667 5.81331 19.3867 6.38665 19.2 6.82665C17.0787 6.50665 14.9213 6.50665 12.8 6.82665C12.6133 6.37331 12.3333 5.81331 12.08 5.37331C12.0667 5.34665 12.0267 5.33331 11.9867 5.33331C9.98666 5.67998 8.07999 6.27998 6.29333 7.10665C6.27999 7.10665 6.26666 7.11998 6.25333 7.13331C2.62666 12.56 1.62666 17.84 2.11999 23.0666C2.11999 23.0933 2.13333 23.12 2.15999 23.1333C4.55999 24.8933 6.86666 25.96 9.14666 26.6666C9.18666 26.68 9.22666 26.6666 9.23999 26.64C9.77333 25.9066 10.2533 25.1333 10.6667 24.32C10.6933 24.2666 10.6667 24.2133 10.6133 24.2C9.85333 23.9066 9.13333 23.56 8.42666 23.16C8.37333 23.1333 8.37333 23.0533 8.41333 23.0133C8.55999 22.9066 8.70666 22.7866 8.85333 22.68C8.87999 22.6533 8.91999 22.6533 8.94666 22.6666C13.5333 24.76 18.48 24.76 23.0133 22.6666C23.04 22.6533 23.08 22.6533 23.1067 22.68C23.2533 22.8 23.4 22.9066 23.5467 23.0266C23.6 23.0666 23.6 23.1466 23.5333 23.1733C22.84 23.5866 22.1067 23.92 21.3467 24.2133C21.2933 24.2266 21.28 24.2933 21.2933 24.3333C21.72 25.1466 22.2 25.92 22.72 26.6533C22.76 26.6666 22.8 26.68 22.84 26.6666C25.1333 25.96 27.44 24.8933 29.84 23.1333C29.8667 23.12 29.88 23.0933 29.88 23.0666C30.4667 17.0266 28.9067 11.7866 25.7467 7.13331C25.7333 7.11998 25.72 7.10665 25.6933 7.10665V7.10665ZM11.36 19.88C9.98666 19.88 8.83999 18.6133 8.83999 17.0533C8.83999 15.4933 9.95999 14.2266 11.36 14.2266C12.7733 14.2266 13.8933 15.5066 13.88 17.0533C13.88 18.6133 12.76 19.88 11.36 19.88ZM20.6533 19.88C19.28 19.88 18.1333 18.6133 18.1333 17.0533C18.1333 15.4933 19.2533 14.2266 20.6533 14.2266C22.0667 14.2266 23.1867 15.5066 23.1733 17.0533C23.1733 18.6133 22.0667 19.88 20.6533 19.88Z" fill="currentColor"></path></svg>
			Discord</a></li>
							<li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			hover:underline
			v2-dropdown-entry" href="https://discuss.huggingface.co/" target="_blank">
		<svg class="mr-1.5 text-gray-300 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" focusable="false" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M12.077 3C7.149 3 3 6.96 3 11.843V21l9.075-.01c4.928 0 8.925-4.11 8.925-8.993C21 7.113 17 3 12.077 3zm3.92 12.859a5.568 5.568 0 0 1-6.102 1.043l-3.595.805l1.001-3.192a5.435 5.435 0 0 1 .11-5.415a5.55 5.55 0 0 1 4.753-2.678v.001h.006a5.533 5.533 0 0 1 5.131 3.438a5.442 5.442 0 0 1-1.304 5.998z" fill="currentColor"></path></svg>
			Forum</a></li>
							<li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			hover:underline
			v2-dropdown-entry" href="https://github.com/huggingface" target="_blank">
		<svg class="mr-1.5 text-gray-300 dark:text-gray-400 text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1.03em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 256 250"><path d="M128.001 0C57.317 0 0 57.307 0 128.001c0 56.554 36.676 104.535 87.535 121.46c6.397 1.185 8.746-2.777 8.746-6.158c0-3.052-.12-13.135-.174-23.83c-35.61 7.742-43.124-15.103-43.124-15.103c-5.823-14.795-14.213-18.73-14.213-18.73c-11.613-7.944.876-7.78.876-7.78c12.853.902 19.621 13.19 19.621 13.19c11.417 19.568 29.945 13.911 37.249 10.64c1.149-8.272 4.466-13.92 8.127-17.116c-28.431-3.236-58.318-14.212-58.318-63.258c0-13.975 5-25.394 13.188-34.358c-1.329-3.224-5.71-16.242 1.24-33.874c0 0 10.749-3.44 35.21 13.121c10.21-2.836 21.16-4.258 32.038-4.307c10.878.049 21.837 1.47 32.066 4.307c24.431-16.56 35.165-13.12 35.165-13.12c6.967 17.63 2.584 30.65 1.255 33.873c8.207 8.964 13.173 20.383 13.173 34.358c0 49.163-29.944 59.988-58.447 63.157c4.591 3.972 8.682 11.762 8.682 23.704c0 17.126-.148 30.91-.148 35.126c0 3.407 2.304 7.398 8.792 6.14C219.37 232.5 256 184.537 256 128.002C256 57.307 198.691 0 128.001 0zm-80.06 182.34c-.282.636-1.283.827-2.194.39c-.929-.417-1.45-1.284-1.15-1.922c.276-.655 1.279-.838 2.205-.399c.93.418 1.46 1.293 1.139 1.931zm6.296 5.618c-.61.566-1.804.303-2.614-.591c-.837-.892-.994-2.086-.375-2.66c.63-.566 1.787-.301 2.626.591c.838.903 1 2.088.363 2.66zm4.32 7.188c-.785.545-2.067.034-2.86-1.104c-.784-1.138-.784-2.503.017-3.05c.795-.547 2.058-.055 2.861 1.075c.782 1.157.782 2.522-.019 3.08zm7.304 8.325c-.701.774-2.196.566-3.29-.49c-1.119-1.032-1.43-2.496-.726-3.27c.71-.776 2.213-.558 3.315.49c1.11 1.03 1.45 2.505.701 3.27zm9.442 2.81c-.31 1.003-1.75 1.459-3.199 1.033c-1.448-.439-2.395-1.613-2.103-2.626c.301-1.01 1.747-1.484 3.207-1.028c1.446.436 2.396 1.602 2.095 2.622zm10.744 1.193c.036 1.055-1.193 1.93-2.715 1.95c-1.53.034-2.769-.82-2.786-1.86c0-1.065 1.202-1.932 2.733-1.958c1.522-.03 2.768.818 2.768 1.868zm10.555-.405c.182 1.03-.875 2.088-2.387 2.37c-1.485.271-2.861-.365-3.05-1.386c-.184-1.056.893-2.114 2.376-2.387c1.514-.263 2.868.356 3.061 1.403z" fill="currentColor"></path></svg>
			Github</a></li></ul></li>
				</ul></div>
	</div></li>
		<li><hr class="w-0.5 h-5 border-none bg-gray-100 dark:bg-gray-800"></li>
		<li><a class="px-2 py-0.5 block cursor-pointer hover:text-gray-500 dark:hover:text-gray-400" href="/login">Log In
				</a></li>
			<li><a class="ml-2 btn" href="/join">Sign Up </a></li></ul></nav></div></header>
	
	
	<main class="flex flex-col flex-1 "><header class="bg-gradient-to-t from-gray-50-to-white via-white dark:via-gray-950 pt-4 "><div class="container relative"><h1 class="flex items-center flex-wrap text-lg leading-tight "><a href="/spaces" class="group flex items-center mb-1"><svg class="mr-1 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M7.80914 18.7462V24.1907H13.2536V18.7462H7.80914Z" fill="#FF3270"></path><path d="M18.7458 18.7462V24.1907H24.1903V18.7462H18.7458Z" fill="#861FFF"></path><path d="M7.80914 7.80982V13.2543H13.2536V7.80982H7.80914Z" fill="#097EFF"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M4 6.41775C4 5.08246 5.08246 4 6.41775 4H14.6457C15.7626 4 16.7026 4.75724 16.9802 5.78629C18.1505 4.67902 19.7302 4 21.4685 4C25.0758 4 28.0003 6.92436 28.0003 10.5317C28.0003 12.27 27.3212 13.8497 26.2139 15.02C27.243 15.2977 28.0003 16.2376 28.0003 17.3545V25.5824C28.0003 26.9177 26.9177 28.0003 25.5824 28.0003H17.0635H14.9367H6.41775C5.08246 28.0003 4 26.9177 4 25.5824V15.1587V14.9367V6.41775ZM7.80952 7.80952V13.254H13.254V7.80952H7.80952ZM7.80952 24.1907V18.7462H13.254V24.1907H7.80952ZM18.7462 24.1907V18.7462H24.1907V24.1907H18.7462ZM18.7462 10.5317C18.7462 9.0283 19.9651 7.80952 21.4685 7.80952C22.9719 7.80952 24.1907 9.0283 24.1907 10.5317C24.1907 12.0352 22.9719 13.254 21.4685 13.254C19.9651 13.254 18.7462 12.0352 18.7462 10.5317Z" fill="black"></path><path d="M21.4681 7.80982C19.9647 7.80982 18.7458 9.02861 18.7458 10.5321C18.7458 12.0355 19.9647 13.2543 21.4681 13.2543C22.9715 13.2543 24.1903 12.0355 24.1903 10.5321C24.1903 9.02861 22.9715 7.80982 21.4681 7.80982Z" fill="#FFD702"></path></svg>
					<span class="text-gray-400 group-hover:text-gray-500 mr-3 font-semibold">Spaces:</span></a>
			<div class="flex items-center mb-1"><img class="w-4 h-4 mr-1.5 rounded" alt="Merve Noyan's picture" src="https://aeiljuispo.cloudimg.io/v7/https://s3.amazonaws.com/moonup/production/uploads/1631694399207-6141a88b3a0ec78603c9e784.png?w=200&amp;h=200&amp;f=face">
					<a href="/merve" class="font-sans text-gray-400 hover:text-blue-600">merve</a>
					<div class="text-gray-300 mx-0.5">/</div></div>
			<div class="max-w-full mb-1"><a class="font-mono font-semibold break-words" href="/spaces/merve/write-with-transformer">write-with-transformer</a>
				<div class="SVELTE_HYDRATER inline mr-4" data-props="{&quot;label&quot;:&quot;objectInfo name&quot;,&quot;noText&quot;:true,&quot;value&quot;:&quot;merve/write-with-transformer&quot;}" data-target="CopyButton"><button class="inline-flex items-center relative text-sm focus:text-green-500  cursor-pointer focus:outline-none
		
		mx-0.5
		text-gray-600
		
	" title="Copy objectInfo name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	<div class="
		absolute pointer-events-none transition-opacity bg-black text-white py-1 px-2 leading-tight rounded font-normal shadow 
		left-1/2 top-full transform -translate-x-1/2 translate-y-2
		opacity-0
	"><div class="absolute bottom-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-black border-4 border-t-0" style="
				border-left-color: transparent;
				border-right-color: transparent;
			"></div>
	Copied</div></button></div></div>
			<div class="SVELTE_HYDRATER mr-3 mb-1" data-props="{&quot;isLikedByUser&quot;:false,&quot;likes&quot;:9,&quot;repoId&quot;:&quot;merve/write-with-transformer&quot;,&quot;repoType&quot;:&quot;space&quot;}" data-target="LikeButton"><div class="inline-flex items-center border leading-none whitespace-nowrap text-sm rounded-md text-gray-500 overflow-hidden bg-white
		"><button class="relative flex items-center px-1.5 py-1 hover:bg-gradient-to-t focus:outline-none from-red-50 to-transparent dark:from-red-900 dark:to-red-800 overflow-hidden"  title="Like"><svg class="mr-1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		<svg class="mr-1 absolute text-red-500 origin-center transform transition ease-in\n\t\t\t\ttranslate-y-10 scale-0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.5,4c-2,0-3.9,0.8-5.3,2.2L16,7.4l-1.1-1.1C12,3.3,7.2,3.3,4.3,6.2c0,0-0.1,0.1-0.1,0.1c-3,3-3,7.8,0,10.8L16,29l11.8-11.9c3-3,3-7.8,0-10.8C26.4,4.8,24.5,4,22.5,4z"></path></svg>
		like
	</button>
	<button class="flex items-center px-1.5 py-1 border-l text-gray-400 focus:outline-none hover:bg-gray-50 dark:hover:bg-gray-700 focus:bg-gray-100 " title="See users who liked this repository">9</button></div>
</div>
			<div class="SVELTE_HYDRATER inline-flex items-center mb-1" data-props="{&quot;initStage&quot;:&quot;running&quot;,&quot;rights&quot;:{&quot;readRepoContent&quot;:false,&quot;writeRepoContent&quot;:false,&quot;readRepoSettings&quot;:false,&quot;writeRepoSettings&quot;:false,&quot;readOrgSettings&quot;:false,&quot;writeOrgSettings&quot;:false},&quot;spaceId&quot;:&quot;merve/write-with-transformer&quot;}" data-target="SpaceStatus">

	<div class="border inline-flex items-center leading-none whitespace-nowrap px-1.5 py-[0.3rem] font-mono text-xs rounded-md text-gray-400 overflow-hidden bg-white mr-3 select-none
		border-green-200 bg-green-50"><div class="inline-block h-1.5 w-1.5 rounded-full ml-0.5 mr-1.5 animate-pulse bg-green-500 "></div>
		<span class="text-green-500">Running</span></div></div></h1>
		
		<div class="border-b border-gray-100"><div class="flex flex-col-reverse lg:flex-row lg:items-center lg:justify-between"><div class="flex items-center h-12 -mb-px overflow-x-auto overflow-y-hidden"><a class="tab-alternate " href="/spaces/merve/write-with-transformer"><svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
			App
		</a>
		<a class="tab-alternate active" href="/spaces/merve/write-with-transformer/tree/main"><svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
			Files and versions
		</a>
		</div>
				<div class="SVELTE_HYDRATER " data-props="{&quot;linkedModels&quot;:[],&quot;linkedDatasets&quot;:[]}" data-target="SpaceHeaderActions">


<div class="relative mb-1.5 mt-1.5 space-y-1 sm:flex sm:space-y-0 sm:space-x-1.5 lg:mb-0 lg:mt-0">
	</div></div>
	</div></div></div></header>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full
	md:grid-cols-12
	 
		space-y-4
		md:gap-6
		mb-16
	"><section class="pt-8 border-gray-100 col-span-full"><header class="pb-2 flex items-center justify-between flex-wrap"><div class="flex flex-wrap items-center"><div class="relative mr-4 mb-2 v2-dropdown">
	<button class="
			text-base
			cursor-pointer w-full btn text-sm
			v2-dropdown-button" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
			<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M7 10l5 5l5-5z" fill="currentColor"></path></svg></button>
	
	
	<div class="absolute top-full mt-1 min-w-full w-auto bg-white rounded-xl overflow-hidden shadow-lg z-10 border border-gray-100
		left-0
		 v2-dropdown-menu hidden"><ul class="min-w-full w-auto">
		<li><ul><li><a class="flex items-center hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer px-3 py-1.5 whitespace-nowrap 
			
			
			v2-dropdown-entry" href="/spaces/merve/write-with-transformer/blob/main/app.py">
		
			main</a></li></ul></li>
		<li><ul class="bg-yellow-50 dark:bg-gray-950"></ul></li>
	</ul></div>
	</div>
		<div class="flex items-center flex-wrap mb-2"><a class="hover:underline text-gray-800" href="/spaces/merve/write-with-transformer/tree/main">write-with-transformer</a>
			<span class="text-gray-300 mx-1 font-light">/</span>
				<span class="font-light dark:text-gray-300">app.py</span>

			</div></div>

	<div class="flex flex-row items-center mb-2">
		</div></header>
			<div class="border border-b-0 dark:border-gray-800 px-3 py-2 flex items-baseline rounded-t-lg bg-gradient-to-t from-gray-100-to-white"><img class="w-4 h-4 rounded-full mt-0.5 mr-2.5 self-center" alt="merve's picture" src="https://aeiljuispo.cloudimg.io/v7/https://s3.amazonaws.com/moonup/production/uploads/1631694399207-6141a88b3a0ec78603c9e784.png?w=200&amp;h=200&amp;f=face">
			<div class="mr-5 truncate flex items-center flex-none"><a class="hover:underline" href="/merve">merve
					</a>
				<div class="mt-0.5 ml-1.5 bg-yellow-50 dark:bg-yellow-800 px-1 uppercase text-xs font-semibold text-yellow-500 dark:text-yellow-400 border border-yellow-200 rounded" title="member of the Hugging Face team">HF staff
					</div>
			</div>
		<a class="mr-4 font-mono text-sm text-gray-500 truncate hover:underline" href="/spaces/merve/write-with-transformer/commit/a40b85e54b9bdb5ffb1de1c2b33670a170310631">Update app.py</a>
		<a class="text-sm border dark:border-gray-800 px-1.5 rounded bg-gray-50 dark:bg-gray-900 hover:underline" href="/spaces/merve/write-with-transformer/commit/a40b85e54b9bdb5ffb1de1c2b33670a170310631">a40b85e</a>
		

		<time class="ml-auto hidden lg:block text-gray-500 dark:text-gray-400 truncate flex-none pl-2" datetime="2021-12-23T17:04:27" title="Thu, 23 Dec 2021 17:04:27 GMT">2 months ago</time></div>
			<div class="flex flex-wrap items-center justify-between px-3 py-1.5 border dark:border-gray-800 text-sm text-gray-800 dark:bg-gray-900"><div class="flex flex-wrap items-center"><a class="flex items-center hover:underline my-1 mr-4" href="/spaces/merve/write-with-transformer/raw/main/app.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
								raw
							</a><a class="flex items-center hover:underline my-1 mr-4" href="/spaces/merve/write-with-transformer/commits/main/app.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
								history
							</a><a class="flex items-center hover:underline my-1 mr-4" href="/spaces/merve/write-with-transformer/blame/main/app.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
								blame
							</a>
					</div>
				<div class="dark:text-gray-300">3 kB</div></div>

			<div class="border border-t-0 rounded-b-lg dark:bg-gray-925 dark:border-gray-800 leading-tight"><div class="py-3"><div class="SVELTE_HYDRATER " data-props="{&quot;lines&quot;:[&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;import&lt;/span&gt; transformers&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;import&lt;/span&gt; streamlit &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;as&lt;/span&gt; st&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;from&lt;/span&gt; transformers &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;import&lt;/span&gt; AutoTokenizer, AutoModelWithLMHead&quot;,&quot;  &quot;,&quot;tokenizer = AutoTokenizer.from_pretrained(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;gpt2-large&amp;quot;&lt;/span&gt;)&quot;,&quot;&lt;span class=\\&quot;hljs-meta\\&quot;&gt;@st.cache&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-function\\&quot;&gt;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;def&lt;/span&gt; &lt;span class=\\&quot;hljs-title\\&quot;&gt;load_model&lt;/span&gt;(&lt;span class=\\&quot;hljs-params\\&quot;&gt;model_name&lt;/span&gt;):&lt;/span&gt;&quot;,&quot;    model = AutoModelWithLMHead.from_pretrained(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;gpt2-large&amp;quot;&lt;/span&gt;)&quot;,&quot;    &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;return&lt;/span&gt; model&quot;,&quot;&quot;,&quot;model = load_model(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;gpt2-large&amp;quot;&lt;/span&gt;)&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-function\\&quot;&gt;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;def&lt;/span&gt; &lt;span class=\\&quot;hljs-title\\&quot;&gt;infer&lt;/span&gt;(&lt;span class=\\&quot;hljs-params\\&quot;&gt;input_ids, max_length, temperature, top_k, top_p&lt;/span&gt;):&lt;/span&gt;&quot;,&quot;&quot;,&quot;    output_sequences = model.generate(&quot;,&quot;        input_ids=input_ids,&quot;,&quot;        max_length=max_length,&quot;,&quot;        temperature=temperature,&quot;,&quot;        top_k=top_k,&quot;,&quot;        top_p=top_p,&quot;,&quot;        do_sample=&lt;span class=\\&quot;hljs-literal\\&quot;&gt;True&lt;/span&gt;,&quot;,&quot;        num_return_sequences=&lt;span class=\\&quot;hljs-number\\&quot;&gt;1&lt;/span&gt;&quot;,&quot;    )&quot;,&quot;&quot;,&quot;    &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;return&lt;/span&gt; output_sequences&quot;,&quot;default_value = &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;See how a modern neural network auto-completes your text 🤗 This site, built by the Hugging Face team, lets you write a whole document directly from your browser, and you can trigger the Transformer anywhere using the Tab key. Its like having a smart machine that completes your thoughts 😀 Get started by typing a custom snippet, check out the repository, or try one of the examples. Have fun!&amp;quot;&lt;/span&gt;&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-comment\\&quot;&gt;#prompts&lt;/span&gt;&quot;,&quot;st.title(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;Write with Transformers 🦄&amp;quot;&lt;/span&gt;)&quot;,&quot;st.write(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;The almighty king of text generation, GPT-2 comes in four available sizes, only three of which have been publicly made available. Feared for its fake news generation capabilities, it currently stands as the most syntactically coherent model. A direct successor to the original GPT, it reinforces the already established pre-training/fine-tuning killer duo. From the paper: Language Models are Unsupervised Multitask Learners by Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei and Ilya Sutskever.&amp;quot;&lt;/span&gt;)&quot;,&quot;&quot;,&quot;sent = st.text_area(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;Text&amp;quot;&lt;/span&gt;, default_value, height = &lt;span class=\\&quot;hljs-number\\&quot;&gt;275&lt;/span&gt;)&quot;,&quot;max_length = st.sidebar.slider(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;Max Length&amp;quot;&lt;/span&gt;, min_value = &lt;span class=\\&quot;hljs-number\\&quot;&gt;10&lt;/span&gt;, max_value=&lt;span class=\\&quot;hljs-number\\&quot;&gt;30&lt;/span&gt;)&quot;,&quot;temperature = st.sidebar.slider(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;Temperature&amp;quot;&lt;/span&gt;, value = &lt;span class=\\&quot;hljs-number\\&quot;&gt;1.0&lt;/span&gt;, min_value = &lt;span class=\\&quot;hljs-number\\&quot;&gt;0.0&lt;/span&gt;, max_value=&lt;span class=\\&quot;hljs-number\\&quot;&gt;1.0&lt;/span&gt;, step=&lt;span class=\\&quot;hljs-number\\&quot;&gt;0.05&lt;/span&gt;)&quot;,&quot;top_k = st.sidebar.slider(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;Top-k&amp;quot;&lt;/span&gt;, min_value = &lt;span class=\\&quot;hljs-number\\&quot;&gt;0&lt;/span&gt;, max_value=&lt;span class=\\&quot;hljs-number\\&quot;&gt;5&lt;/span&gt;, value = &lt;span class=\\&quot;hljs-number\\&quot;&gt;0&lt;/span&gt;)&quot;,&quot;top_p = st.sidebar.slider(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;Top-p&amp;quot;&lt;/span&gt;, min_value = &lt;span class=\\&quot;hljs-number\\&quot;&gt;0.0&lt;/span&gt;, max_value=&lt;span class=\\&quot;hljs-number\\&quot;&gt;1.0&lt;/span&gt;, step = &lt;span class=\\&quot;hljs-number\\&quot;&gt;0.05&lt;/span&gt;, value = &lt;span class=\\&quot;hljs-number\\&quot;&gt;0.9&lt;/span&gt;)&quot;,&quot;&quot;,&quot;encoded_prompt = tokenizer.encode(sent, add_special_tokens=&lt;span class=\\&quot;hljs-literal\\&quot;&gt;False&lt;/span&gt;, return_tensors=&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;pt&amp;quot;&lt;/span&gt;)&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;if&lt;/span&gt; encoded_prompt.size()[&lt;span class=\\&quot;hljs-number\\&quot;&gt;-1&lt;/span&gt;] == &lt;span class=\\&quot;hljs-number\\&quot;&gt;0&lt;/span&gt;:&quot;,&quot;    input_ids = &lt;span class=\\&quot;hljs-literal\\&quot;&gt;None&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;else&lt;/span&gt;:&quot;,&quot;    input_ids = encoded_prompt&quot;,&quot;&quot;,&quot;&quot;,&quot;output_sequences = infer(input_ids, max_length, temperature, top_k, top_p)&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;for&lt;/span&gt; generated_sequence_idx, generated_sequence &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;in&lt;/span&gt; &lt;span class=\\&quot;hljs-built_in\\&quot;&gt;enumerate&lt;/span&gt;(output_sequences):&quot;,&quot;    print(&lt;span class=\\&quot;hljs-string\\&quot;&gt;f&amp;quot;=== GENERATED SEQUENCE &lt;span class=\\&quot;hljs-subst\\&quot;&gt;{generated_sequence_idx + &lt;span class=\\&quot;hljs-number\\&quot;&gt;1&lt;/span&gt;}&lt;/span&gt; ===&amp;quot;&lt;/span&gt;)&quot;,&quot;    generated_sequences = generated_sequence.tolist()&quot;,&quot;&quot;,&quot;    &lt;span class=\\&quot;hljs-comment\\&quot;&gt;# Decode text&lt;/span&gt;&quot;,&quot;    text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=&lt;span class=\\&quot;hljs-literal\\&quot;&gt;True&lt;/span&gt;)&quot;,&quot;&quot;,&quot;    &lt;span class=\\&quot;hljs-comment\\&quot;&gt;# Remove all text after the stop token&lt;/span&gt;&quot;,&quot;    &lt;span class=\\&quot;hljs-comment\\&quot;&gt;#text = text[: text.find(args.stop_token) if args.stop_token else None]&lt;/span&gt;&quot;,&quot;&quot;,&quot;    &lt;span class=\\&quot;hljs-comment\\&quot;&gt;# Add the prompt at the beginning of the sequence. Remove the excess text that was used for pre-processing&lt;/span&gt;&quot;,&quot;    total_sequence = (&quot;,&quot;        sent + text[&lt;span class=\\&quot;hljs-built_in\\&quot;&gt;len&lt;/span&gt;(tokenizer.decode(encoded_prompt[&lt;span class=\\&quot;hljs-number\\&quot;&gt;0&lt;/span&gt;], clean_up_tokenization_spaces=&lt;span class=\\&quot;hljs-literal\\&quot;&gt;True&lt;/span&gt;)) :]&quot;,&quot;    )&quot;,&quot;&quot;,&quot;    generated_sequences.append(total_sequence)&quot;,&quot;    print(total_sequence)&quot;,&quot;&quot;,&quot;&quot;,&quot;st.write(generated_sequences[&lt;span class=\\&quot;hljs-number\\&quot;&gt;-1&lt;/span&gt;])&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;]}" data-target="BlobContent"><div class="relative text-sm"><div class="overflow-x-auto"><table class="border-collapse font-mono"><tbody><tr class="" id="L1"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">1</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">import</span> transformers</td>
					</tr><tr class="" id="L2"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">2</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">import</span> streamlit <span class="hljs-keyword">as</span> st</td>
					</tr><tr class="" id="L3"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">3</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L4"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">4</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">from</span> transformers <span class="hljs-keyword">import</span> AutoTokenizer, AutoModelWithLMHead</td>
					</tr><tr class="" id="L5"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">5</td>
						<td class="px-3 overflow-visible whitespace-pre">  </td>
					</tr><tr class="" id="L6"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">6</td>
						<td class="px-3 overflow-visible whitespace-pre">tokenizer = AutoTokenizer.from_pretrained(<span class="hljs-string">&quot;gpt2-large&quot;</span>)</td>
					</tr><tr class="" id="L7"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">7</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-meta">@st.cache</span></td>
					</tr><tr class="" id="L8"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">8</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">load_model</span>(<span class="hljs-params">model_name</span>):</span></td>
					</tr><tr class="" id="L9"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">9</td>
						<td class="px-3 overflow-visible whitespace-pre">    model = AutoModelWithLMHead.from_pretrained(<span class="hljs-string">&quot;gpt2-large&quot;</span>)</td>
					</tr><tr class="" id="L10"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">10</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-keyword">return</span> model</td>
					</tr><tr class="" id="L11"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">11</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L12"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">12</td>
						<td class="px-3 overflow-visible whitespace-pre">model = load_model(<span class="hljs-string">&quot;gpt2-large&quot;</span>)</td>
					</tr><tr class="" id="L13"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">13</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L14"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">14</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">infer</span>(<span class="hljs-params">input_ids, max_length, temperature, top_k, top_p</span>):</span></td>
					</tr><tr class="" id="L15"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">15</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L16"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">16</td>
						<td class="px-3 overflow-visible whitespace-pre">    output_sequences = model.generate(</td>
					</tr><tr class="" id="L17"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">17</td>
						<td class="px-3 overflow-visible whitespace-pre">        input_ids=input_ids,</td>
					</tr><tr class="" id="L18"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">18</td>
						<td class="px-3 overflow-visible whitespace-pre">        max_length=max_length,</td>
					</tr><tr class="" id="L19"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">19</td>
						<td class="px-3 overflow-visible whitespace-pre">        temperature=temperature,</td>
					</tr><tr class="" id="L20"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">20</td>
						<td class="px-3 overflow-visible whitespace-pre">        top_k=top_k,</td>
					</tr><tr class="" id="L21"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">21</td>
						<td class="px-3 overflow-visible whitespace-pre">        top_p=top_p,</td>
					</tr><tr class="" id="L22"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">22</td>
						<td class="px-3 overflow-visible whitespace-pre">        do_sample=<span class="hljs-literal">True</span>,</td>
					</tr><tr class="" id="L23"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">23</td>
						<td class="px-3 overflow-visible whitespace-pre">        num_return_sequences=<span class="hljs-number">1</span></td>
					</tr><tr class="" id="L24"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">24</td>
						<td class="px-3 overflow-visible whitespace-pre">    )</td>
					</tr><tr class="" id="L25"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">25</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L26"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">26</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-keyword">return</span> output_sequences</td>
					</tr><tr class="" id="L27"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">27</td>
						<td class="px-3 overflow-visible whitespace-pre">default_value = <span class="hljs-string">&quot;See how a modern neural network auto-completes your text 🤗 This site, built by the Hugging Face team, lets you write a whole document directly from your browser, and you can trigger the Transformer anywhere using the Tab key. Its like having a smart machine that completes your thoughts 😀 Get started by typing a custom snippet, check out the repository, or try one of the examples. Have fun!&quot;</span></td>
					</tr><tr class="" id="L28"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">28</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L29"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">29</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-comment">#prompts</span></td>
					</tr><tr class="" id="L30"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">30</td>
						<td class="px-3 overflow-visible whitespace-pre">st.title(<span class="hljs-string">&quot;Write with Transformers 🦄&quot;</span>)</td>
					</tr><tr class="" id="L31"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">31</td>
						<td class="px-3 overflow-visible whitespace-pre">st.write(<span class="hljs-string">&quot;The almighty king of text generation, GPT-2 comes in four available sizes, only three of which have been publicly made available. Feared for its fake news generation capabilities, it currently stands as the most syntactically coherent model. A direct successor to the original GPT, it reinforces the already established pre-training/fine-tuning killer duo. From the paper: Language Models are Unsupervised Multitask Learners by Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei and Ilya Sutskever.&quot;</span>)</td>
					</tr><tr class="" id="L32"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">32</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L33"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">33</td>
						<td class="px-3 overflow-visible whitespace-pre">sent = st.text_area(<span class="hljs-string">&quot;Text&quot;</span>, default_value, height = <span class="hljs-number">275</span>)</td>
					</tr><tr class="" id="L34"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">34</td>
						<td class="px-3 overflow-visible whitespace-pre">max_length = st.sidebar.slider(<span class="hljs-string">&quot;Max Length&quot;</span>, min_value = <span class="hljs-number">10</span>, max_value=<span class="hljs-number">30</span>)</td>
					</tr><tr class="" id="L35"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">35</td>
						<td class="px-3 overflow-visible whitespace-pre">temperature = st.sidebar.slider(<span class="hljs-string">&quot;Temperature&quot;</span>, value = <span class="hljs-number">1.0</span>, min_value = <span class="hljs-number">0.0</span>, max_value=<span class="hljs-number">1.0</span>, step=<span class="hljs-number">0.05</span>)</td>
					</tr><tr class="" id="L36"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">36</td>
						<td class="px-3 overflow-visible whitespace-pre">top_k = st.sidebar.slider(<span class="hljs-string">&quot;Top-k&quot;</span>, min_value = <span class="hljs-number">0</span>, max_value=<span class="hljs-number">5</span>, value = <span class="hljs-number">0</span>)</td>
					</tr><tr class="" id="L37"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">37</td>
						<td class="px-3 overflow-visible whitespace-pre">top_p = st.sidebar.slider(<span class="hljs-string">&quot;Top-p&quot;</span>, min_value = <span class="hljs-number">0.0</span>, max_value=<span class="hljs-number">1.0</span>, step = <span class="hljs-number">0.05</span>, value = <span class="hljs-number">0.9</span>)</td>
					</tr><tr class="" id="L38"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">38</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L39"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">39</td>
						<td class="px-3 overflow-visible whitespace-pre">encoded_prompt = tokenizer.encode(sent, add_special_tokens=<span class="hljs-literal">False</span>, return_tensors=<span class="hljs-string">&quot;pt&quot;</span>)</td>
					</tr><tr class="" id="L40"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">40</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">if</span> encoded_prompt.size()[<span class="hljs-number">-1</span>] == <span class="hljs-number">0</span>:</td>
					</tr><tr class="" id="L41"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">41</td>
						<td class="px-3 overflow-visible whitespace-pre">    input_ids = <span class="hljs-literal">None</span></td>
					</tr><tr class="" id="L42"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">42</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">else</span>:</td>
					</tr><tr class="" id="L43"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">43</td>
						<td class="px-3 overflow-visible whitespace-pre">    input_ids = encoded_prompt</td>
					</tr><tr class="" id="L44"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">44</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L45"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">45</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L46"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">46</td>
						<td class="px-3 overflow-visible whitespace-pre">output_sequences = infer(input_ids, max_length, temperature, top_k, top_p)</td>
					</tr><tr class="" id="L47"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">47</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L48"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">48</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L49"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">49</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L50"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">50</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">for</span> generated_sequence_idx, generated_sequence <span class="hljs-keyword">in</span> <span class="hljs-built_in">enumerate</span>(output_sequences):</td>
					</tr><tr class="" id="L51"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">51</td>
						<td class="px-3 overflow-visible whitespace-pre">    print(<span class="hljs-string">f&quot;=== GENERATED SEQUENCE <span class="hljs-subst">{generated_sequence_idx + <span class="hljs-number">1</span>}</span> ===&quot;</span>)</td>
					</tr><tr class="" id="L52"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">52</td>
						<td class="px-3 overflow-visible whitespace-pre">    generated_sequences = generated_sequence.tolist()</td>
					</tr><tr class="" id="L53"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">53</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L54"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">54</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-comment"># Decode text</span></td>
					</tr><tr class="" id="L55"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">55</td>
						<td class="px-3 overflow-visible whitespace-pre">    text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=<span class="hljs-literal">True</span>)</td>
					</tr><tr class="" id="L56"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">56</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L57"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">57</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-comment"># Remove all text after the stop token</span></td>
					</tr><tr class="" id="L58"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">58</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-comment">#text = text[: text.find(args.stop_token) if args.stop_token else None]</span></td>
					</tr><tr class="" id="L59"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">59</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L60"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">60</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-comment"># Add the prompt at the beginning of the sequence. Remove the excess text that was used for pre-processing</span></td>
					</tr><tr class="" id="L61"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">61</td>
						<td class="px-3 overflow-visible whitespace-pre">    total_sequence = (</td>
					</tr><tr class="" id="L62"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">62</td>
						<td class="px-3 overflow-visible whitespace-pre">        sent + text[<span class="hljs-built_in">len</span>(tokenizer.decode(encoded_prompt[<span class="hljs-number">0</span>], clean_up_tokenization_spaces=<span class="hljs-literal">True</span>)) :]</td>
					</tr><tr class="" id="L63"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">63</td>
						<td class="px-3 overflow-visible whitespace-pre">    )</td>
					</tr><tr class="" id="L64"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">64</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L65"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">65</td>
						<td class="px-3 overflow-visible whitespace-pre">    generated_sequences.append(total_sequence)</td>
					</tr><tr class="" id="L66"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">66</td>
						<td class="px-3 overflow-visible whitespace-pre">    print(total_sequence)</td>
					</tr><tr class="" id="L67"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">67</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L68"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">68</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L69"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">69</td>
						<td class="px-3 overflow-visible whitespace-pre">st.write(generated_sequences[<span class="hljs-number">-1</span>])</td>
					</tr><tr class="" id="L70"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">70</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L71"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">71</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L72"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">72</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr></tbody></table></div>
	</div></div></div></div></section></div></main>
	</div>

		<script>
			import("/front/build/module/index.c4dc3d96.js");
			window.supportsDynamicImport = true;
		</script>
		<script>
			if (!window.supportsDynamicImport) {
				const systemJsLoaderTag = document.createElement("script");
				systemJsLoaderTag.src =
					"https://unpkg.com/systemjs@2.0.0/dist/s.min.js";
				systemJsLoaderTag.addEventListener("load", function () {
					System.import("./front/build/nomodule/index.c4dc3d96.js");
				});
				document.head.appendChild(systemJsLoaderTag);
			}
		</script>

		<script type="text/javascript">
			/// LinkedIn (part 1)
			_linkedin_partner_id = "3734489";
			window._linkedin_data_partner_ids =
				window._linkedin_data_partner_ids || [];
			window._linkedin_data_partner_ids.push(_linkedin_partner_id);
		</script>

		<script>
			if (
				!(
					["localhost", "huggingface.test"].includes(
						window.location.hostname
					) || window.location.hostname.includes("ngrok.io")
				)
			) {
				(function (i, s, o, g, r, a, m) {
					i["GoogleAnalyticsObject"] = r;
					(i[r] =
						i[r] ||
						function () {
							(i[r].q = i[r].q || []).push(arguments);
						}),
						(i[r].l = 1 * new Date());
					(a = s.createElement(o)), (m = s.getElementsByTagName(o)[0]);
					a.async = 1;
					a.src = g;
					m.parentNode.insertBefore(a, m);
				})(
					window,
					document,
					"script",
					"https://www.google-analytics.com/analytics.js",
					"ganalytics"
				);
				ganalytics("create", "UA-83738774-2", "auto");
				ganalytics("send", "pageview");

				/// LinkedIn (part 2)
				(function (l) {
					if (!l) {
						window.lintrk = function (a, b) {
							window.lintrk.q.push([a, b]);
						};
						window.lintrk.q = [];
					}
					var s = document.getElementsByTagName("script")[0];
					var b = document.createElement("script");
					b.type = "text/javascript";
					b.async = true;
					b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
					s.parentNode.insertBefore(b, s);
				})(window.lintrk);

				/// Twitter
				!(function (e, t, n, s, u, a) {
					e.twq ||
						((s = e.twq =
							function () {
								s.exe ? s.exe.apply(s, arguments) : s.queue.push(arguments);
							}),
						(s.version = "1.1"),
						(s.queue = []),
						(u = t.createElement(n)),
						(u.async = !0),
						(u.src = "//static.ads-twitter.com/uwt.js"),
						(a = t.getElementsByTagName(n)[0]),
						a.parentNode.insertBefore(u, a));
				})(window, document, "script");
				twq("init", "o6bfm");
				twq("track", "PageView");
			}
		</script>

		<noscript>
			<!-- LinkedIn (part 3) -->
			<img
				height="1"
				width="1"
				style="display: none"
				alt=""
				src="https://px.ads.linkedin.com/collect/?pid=3734489&fmt=gif"
			/>
		</noscript>
	</body>
</html>
