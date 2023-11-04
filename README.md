<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="SpotifyBangerPrediction_0"></a>Spotify-Banger-Prediction</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">Welcome to the spotify banger prediction. Trained on 800 rows of top songs from the year 2023!</p>
<h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="Model_Features_4"></a>Model Features</h2>
<ul>
<li class="has-line-data" data-line-start="6" data-line-end="7">Song Bpm</li>
<li class="has-line-data" data-line-start="7" data-line-end="8">Artist Count</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">Speechiness %</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">In How many spotify playlists</li>
<li class="has-line-data" data-line-start="10" data-line-end="11">Song valence %</li>
<li class="has-line-data" data-line-start="11" data-line-end="12">Accousticness %</li>
<li class="has-line-data" data-line-start="12" data-line-end="14">Song Energy %</li>
</ul>
<h2 class="code-line" data-line-start=14 data-line-end=15 ><a id="Test_it_out_14"></a>Test it out!</h2>
<p class="has-line-data" data-line-start="16" data-line-end="17"><a href="https://huggingface.co/spaces/BelieveImSteve/Predict_Spotify_Song_Danceability">App Link</a></p>
<h2 class="code-line" data-line-start=18 data-line-end=19 ><a id="Installation_For_running_it_locally_18"></a>Installation (For running it locally)</h2>
<p class="has-line-data" data-line-start="20" data-line-end="21">Install the dependencies and devDependencies and start the server.</p>
<pre><code class="has-line-data" data-line-start="23" data-line-end="25" class="language-sh">pip install streamlit
</code></pre>
<pre><code class="has-line-data" data-line-start="26" data-line-end="28" class="language-sh">pip install -U scikit-learn
</code></pre>
<pre><code class="has-line-data" data-line-start="29" data-line-end="31" class="language-sh">pip install joblib
</code></pre>
<p class="has-line-data" data-line-start="32" data-line-end="33">For running the streamlit app…</p>
<pre><code class="has-line-data" data-line-start="35" data-line-end="37" class="language-sh">streamlit run app.py
</code></pre>
<h4 class="code-line" data-line-start=37 data-line-end=38 ><a id="Building_for_source_37"></a>Building for source</h4>
<p class="has-line-data" data-line-start="39" data-line-end="40">The model, notebook and csv is open to use and play around.</p>
<pre><code class="has-line-data" data-line-start="42" data-line-end="45" class="language-sh">Model:
Spotify_SongDanceability_Predicter.pkl .
</code></pre>
<pre><code class="has-line-data" data-line-start="46" data-line-end="49" class="language-sh">Model Info:
model_info.pkl
</code></pre>
<p class="has-line-data" data-line-start="50" data-line-end="51">Test the model code python:</p>
<pre><code class="has-line-data" data-line-start="52" data-line-end="68" class="language-sh"><span class="hljs-built_in">test</span>_data = {
        <span class="hljs-string">'bpm'</span>: <span class="hljs-number">65</span>,
        <span class="hljs-string">'energy_%'</span>: <span class="hljs-number">75</span>,
        <span class="hljs-string">'acousticness_%'</span>: <span class="hljs-number">50</span>,
        <span class="hljs-string">'in_spotify_playlists'</span>: np.log(<span class="hljs-number">100</span>),
        <span class="hljs-string">'speechiness_%'</span>: np.log(<span class="hljs-number">60</span>),
        <span class="hljs-string">'valence_%'</span>: <span class="hljs-number">50</span>,
        <span class="hljs-string">'artist_count'</span>: np.log(<span class="hljs-number">2</span>)
    }
    
input_df = pd.DataFrame(<span class="hljs-built_in">test</span>_data, index=[<span class="hljs-number">0</span>])

prediction = model.predict(input_df)

<span class="hljs-built_in">print</span>(prediction, <span class="hljs-string">" %"</span>)
</code></pre>
