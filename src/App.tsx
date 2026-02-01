import { Github, Linkedin, Moon, Sun } from 'lucide-react';
import { useEffect, useState } from 'react';
import { calcExp } from './utils';
import './index.css';

interface ExperienceCardProps {
  role: string;
  company: string;
  period: string;
  bullets: string[];
  skills: string[];
}

function ExperienceCard({ role, company, period, bullets, skills }: ExperienceCardProps) {
  return (
    <div className="rounded-lg border bg-card text-card-foreground shadow-sm p-6">
      <h3 className="text-lg font-semibold tracking-tight">{role}</h3>
      <p className="text-sm text-muted-foreground mt-1">{company}</p>
      <p className="text-xs text-muted-foreground mt-1">{period}</p>
      <div className="my-4 h-px bg-border" />
      <ul className="text-sm space-y-2 mb-4 text-foreground">
        {bullets.map((bullet, idx) => (
          <li key={idx} className="flex gap-2">
            <span className="text-muted-foreground mt-1.5">•</span>
            <span>{bullet}</span>
          </li>
        ))}
      </ul>
      <div className="flex flex-wrap gap-2">
        {skills.map((skill, idx) => (
          <span 
            key={idx} 
            className="inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 bg-purple-100 text-purple-900 dark:bg-purple-900/30 dark:text-purple-400 border-transparent"
          >
            {skill}
          </span>
        ))}
      </div>
    </div>
  );
}

function App() {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    // Check for saved theme preference or system preference
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const isDark = savedTheme === 'dark' || (!savedTheme && prefersDark);
    setDarkMode(isDark);
    document.documentElement.classList.toggle('dark', isDark);
  }, []);

  const toggleDarkMode = () => {
    const newMode = !darkMode;
    setDarkMode(newMode);
    document.documentElement.classList.toggle('dark', newMode);
    localStorage.setItem('theme', newMode ? 'dark' : 'light');
  };

  return (
    <div className="min-h-screen w-full bg-background">
      {/* Navbar */}
      <nav className="sticky top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="max-w-7xl mx-auto px-6 flex h-16 items-center justify-between">
          <div>
            <h1 className="text-lg font-semibold tracking-tight">Raphael Clifton</h1>
            <p className="text-sm text-muted-foreground">Data Engineer</p>
          </div>
          <div className="flex items-center gap-6">
            <a href="#experience" className="text-sm font-medium transition-colors hover:text-primary">Experience</a>
            <a href="#education" className="text-sm font-medium transition-colors hover:text-primary">Education</a>
            <a href="#skills" className="text-sm font-medium transition-colors hover:text-primary">Skills</a>
            <button 
              onClick={toggleDarkMode} 
              className="inline-flex h-9 w-9 items-center justify-center rounded-md text-sm font-medium transition-colors hover:bg-accent hover:text-accent-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring"
            >
              {darkMode ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
            </button>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <header className="w-full border-b bg-gradient-to-br from-violet-600 via-purple-600 to-purple-700 text-white">
        <div className="max-w-7xl mx-auto px-6 flex flex-col items-center justify-center py-24 text-center">
          <h2 className="text-5xl sm:text-6xl mb-4 font-bold tracking-tight" style={{ fontFamily: 'Brush Script MT, cursive' }}>Hello, World!</h2>
          <p className="text-xl mb-2 text-white/90">👋🏽 My name is Raphael. I'm a Data Engineer and tech enthusiast.</p>
          <p className="text-lg mb-8 max-w-2xl text-white/80">Building reliable, scalable data systems that power business decisions.</p>
          <div className="flex items-center gap-3">
            <a 
              href="#experience" 
              className="inline-flex h-10 items-center justify-center rounded-md bg-white px-6 text-sm font-semibold text-slate-900 shadow transition-colors hover:bg-white/90"
            >
              View Experience
            </a>
            <a 
              href="https://github.com/RaphCodec" 
              aria-label="GitHub" 
              target="_blank" 
              rel="noreferrer" 
              className="inline-flex h-10 w-10 items-center justify-center rounded-md bg-white/10 backdrop-blur transition-colors hover:bg-white/20"
            >
              <Github className="h-5 w-5 text-white" />
            </a>
            <a 
              href="https://www.linkedin.com/in/raphael-clifton/" 
              aria-label="LinkedIn" 
              target="_blank" 
              rel="noreferrer" 
              className="inline-flex h-10 w-10 items-center justify-center rounded-md bg-white/10 backdrop-blur transition-colors hover:bg-white/20"
            >
              <Linkedin className="h-5 w-5 text-white" />
            </a>
          </div>
        </div>
      </header>

      {/* Experience */}
      <section id="experience" className="w-full py-16 bg-background">
        <div className="max-w-7xl mx-auto px-6">
          <h3 className="text-3xl font-bold tracking-tight text-center mb-10">Work Experience</h3>
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          <ExperienceCard
            role="Deputy Director of Data Engineering and DevOps"
            company="New York City Department of Transportation"
            period={calcExp('2026-01-01', new Date().toISOString().split('T')[0])}
            bullets={[
              'Manage a team of data engineers and DevOps professionals',
              'Implement and migrate data pipelines to Apache Airflow hosted on Azure AKS',
              'Migrate analytics workloads to Snowflake from SQL Server',
              'Develop DevOps CI/CD pipelines using GitHub Actions',
              'Leverage GitHub Projects for task management and sprint planning',
            ]}
            skills={['Python', 'Airflow', 'Azure', 'Snowflake', 'FastAPI']}
          />
          <ExperienceCard
            role="Data Engineer"
            company="New York City Department of Transportation"
            period={calcExp('2023-07-01', '2026-01-01')}
            bullets={[
              'Create and manage databases for analytics and web development',
              'Create and maintain various data pipelines using Python and SQL',
              'Built interactive Org Chart application for workforce planning',
              'Contributed to Power BI dashboards for 311, Congestion Pricing, and KPIs',
            ]}
            skills={['Python', 'Airflow', 'Azure', 'Snowflake', 'FastAPI']}
          />
          <ExperienceCard
            role="Data Engineering Intern | College Aide"
            company="New York City Department of Transportation"
            period={calcExp('2022-07-01', '2023-07-01')}
            bullets={[
              'Developed Python data pipelines for the central data unit',
              'Reduced pipeline load times by 50-95%',
              'Improved data quality and ETL reliability',
            ]}
            skills={['Python', 'SQL']}
          />
          <ExperienceCard
            role="Tutor"
            company="CUNY Tutor Corps"
            period={calcExp('2019-10-01', '2021-06-01')}
            bullets={[
              'Conducted group and one-on-one tutoring sessions remotely and in-person',
              'Helped students develop mathematical and critical thinking skills',
            ]}
            skills={['Communication', 'Teaching']}
          />
          <ExperienceCard
            role="Operations Intern"
            company="CUNY Summer Corps"
            period={calcExp('2019-07-01', '2019-08-31')}
            bullets={[
              'Restocked and fixed printers daily',
              'Assembled books for events as needed',
              'Sorted and organized incoming and outgoing mail 3-4 times daily',
            ]}
            skills={['Operations', 'Organization']}
          />
          <ExperienceCard
            role="Front Desk Attendant"
            company="Baruch College (Economics and Finance Department)"
            period={calcExp('2018-10-01', '2019-05-31')}
            bullets={[
              'Answered student questions in person and on the phone',
              'Restocked office supplies 2-3 times a day',
            ]}
            skills={['Customer Service', 'Administration']}
          />
          </div>
        </div>
      </section>

      {/* Education */}
      <section id="education" className="w-full py-16 bg-muted/30">
        <div className="max-w-7xl mx-auto px-6">
          <h3 className="text-3xl font-bold tracking-tight text-center mb-10">Education</h3>
          <div className="grid gap-6 md:grid-cols-2">
            <div className="rounded-lg border bg-card text-card-foreground shadow-sm p-6">
              <h4 className="text-lg font-semibold mb-2">Master's Degree</h4>
              <p className="text-sm text-foreground">CUNY Baruch College: Zicklin School of Business</p>
              <p className="text-sm text-muted-foreground mt-3">MS, Information Systems — Data Analytics</p>
              <p className="text-sm text-muted-foreground mt-1">Jan 2022 - Jun 2023</p>
            </div>
            <div className="rounded-lg border bg-card text-card-foreground shadow-sm p-6">
              <h4 className="text-lg font-semibold mb-2">Bachelor's Degree</h4>
              <p className="text-sm text-foreground">CUNY Baruch College: Zicklin School of Business</p>
              <p className="text-sm text-muted-foreground mt-3">BBA, Economics</p>
              <p className="text-sm text-muted-foreground mt-1">Sep 2017 - Jun 2021</p>
            </div>
          </div>
        </div>
      </section>

      {/* Skills */}
      <section id="skills" className="w-full py-16 bg-background">
        <div className="max-w-7xl mx-auto px-6">
          <h3 className="text-3xl font-bold tracking-tight text-center mb-10">Skills</h3>
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {Object.entries({
              'Programming': ['Python', 'C#', 'SQL'],
              'Orchestration & ETL': ['Apache Airflow', 'Azure Data Factory'],
              'Data Warehousing': ['Snowflake', 'SQL Server', 'DuckDB', 'Postgres'],
              'Backend': ['FastAPI', 'Django'],
              'Frontend': ['React', 'Reflex'],
              'Version Control': ['GitHub', 'GitHub Actions', 'Azure DevOps'],
            }).map(([category, skills]) => (
              <div key={category} className="rounded-lg border bg-card text-card-foreground shadow-sm p-6">
                <h4 className="text-lg font-semibold mb-4">{category}</h4>
                <div className="flex flex-wrap gap-2">
                  {skills.map((skill) => (
                    <span 
                      key={skill} 
                      className="inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 bg-blue-100 text-blue-900 dark:bg-blue-900/30 dark:text-blue-400 border-transparent"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="w-full border-t py-8 bg-muted/30">
        <div className="max-w-7xl mx-auto px-6 text-center text-sm text-muted-foreground">
          © 2026 Raphael Clifton - Data Engineer
        </div>
      </footer>
    </div>
  );
}

export default App;
