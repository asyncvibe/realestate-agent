# Real Estate Investment Analysis AI

An intelligent real estate analysis system powered by CrewAI that helps analyze retail property investments using AI agents. The system performs comprehensive market research, property analysis, and investment recommendations.

## Features

- Automated retail property investment analysis
- Market trend evaluation and economic indicators assessment
- Demographic data and consumer spending pattern analysis
- Comprehensive property evaluation including:
  - Foot traffic analysis
  - Accessibility assessment
  - Location analysis
  - Tenant mix evaluation
- Financial analysis including ROI projections
- Risk assessment and mitigation strategies
- Detailed investment recommendation reports

## Requirements

- Python 3.12+
- CrewAI 0.11.0+
- Langchain-groq
- Python-dotenv
- CrewAI-tools

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd realestate-agent
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your API keys:
```
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

## Project Structure

- `agents.py`: Defines the AI agents (Property Researcher and Property Analyst)
- `tasks.py`: Defines the analysis tasks and their requirements
- `tools.py`: Contains tools used by the agents
- `crew.py`: Sets up and manages the AI crew

## Usage

Run the analysis for a specific location:

```bash
python crew.py
```

The default location is set to "Melbourne" but can be modified in the `crew.py` file.

## Current Agents

1. **Property Researcher**: 
   - Specializes in retail property investment analysis
   - 15 years of simulated experience
   - Evaluates locations, market trends, and investment potential
   - Uses modern retail analytics and traditional metrics

2. **Property Analyst**:
   - Creates comprehensive investment reports
   - Focuses on financial analysis and risk assessment
   - Provides actionable insights and recommendations

## TODO List

### Immediate Improvements
- [ ] Add support for multiple locations analysis in parallel
- [ ] Implement property comparison feature
- [ ] Add visualization generation for market trends
- [ ] Create a web interface for easier interaction

### Future Enhancements
- [ ] Integrate with real estate APIs for live data
- [ ] Add machine learning models for price prediction
- [ ] Implement automated report generation in PDF format
- [ ] Add support for residential property analysis
- [ ] Create an API endpoint for the analysis service

### Technical Debt
- [ ] Add comprehensive unit tests
- [ ] Implement error handling and logging
- [ ] Add input validation for API keys and parameters
- [ ] Create documentation using Sphinx
- [ ] Optimize agent performance and reduce API calls

### User Experience
- [ ] Add progress tracking for analysis tasks
- [ ] Create interactive visualizations
- [ ] Implement customizable report templates
- [ ] Add support for different output formats
- [ ] Create a command-line interface with arguments

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This is an AI-powered analysis tool and should not be used as the sole decision-maker for real estate investments. Always consult with real estate professionals and perform due diligence before making investment decisions.