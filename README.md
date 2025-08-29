### 🔧 File Structure

<pre class="overflow-visible!" data-start="364" data-end="840"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>self_improvement_ai/
│
├── main.py                 </span><span># CLI or script entry point</span><span>
├── themes/
│   ├── motivation_energy.py
│   ├── confidence.py
│   ├── performance.py
│   └── mindset.py
│
├── prompts/
│   ├── motivation_prompt.txt
│   ├── confidence_prompt.txt
│   ├── performance_prompt.txt
│   └── mindset_prompt.txt
│
├── tools/
│   └── ollama_client.py    </span><span># Mistral integration</span><span>
│
├── tracker/
│   └── habit_tracker.json  </span><span># Simple storage (or use CSV)</span><span>
│
└── README.md
</span></span></code></div></div></pre>
