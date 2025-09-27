# Contributing to AWS IAM CloudFormation

Thank you for your interest in contributing to this enterprise zero-trust security architecture project!

## 🤝 How to Contribute

### 1. Fork and Clone
```bash
git clone https://github.com/codewithramesh-pradhan/aws-iam-cloudformation.git
cd aws-iam-cloudformation
```

### 2. Create Feature Branch
```bash
git checkout -b feature/your-enhancement
```

### 3. Make Changes
- Follow existing code style and conventions
- Update documentation for any new features
- Add tests for new functionality
- Ensure security best practices

### 4. Test Changes
```bash
# Validate security configurations
./scripts/security-validation.sh --comprehensive

# Generate updated diagrams
python3 generate_architecture_diagram.py
```

### 5. Commit and Push
```bash
git add .
git commit -m "feat: add your enhancement description"
git push origin feature/your-enhancement
```

### 6. Create Pull Request
- Provide clear description of changes
- Reference any related issues
- Include screenshots for UI changes
- Ensure all checks pass

## 📋 Contribution Guidelines

### Code Style
- Use clear, descriptive variable names
- Add comments for complex logic
- Follow AWS best practices
- Maintain security-first approach

### Documentation
- Update README.md for new features
- Add screenshots for visual changes
- Update architecture diagrams if needed
- Include compliance considerations

### Security
- Never commit sensitive information
- Follow principle of least privilege
- Validate all security configurations
- Test in non-production environments first

## 🐛 Bug Reports

When reporting bugs, please include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (AWS region, CLI version, etc.)
- Screenshots if applicable

## 💡 Feature Requests

For new features, please provide:
- Clear use case description
- Business justification
- Proposed implementation approach
- Potential security implications
- Compliance considerations

## 📞 Getting Help

- 📧 Email: security@your-domain.com
- 🐛 GitHub Issues for bugs and features
- 📚 Check existing documentation in `/docs/`

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Project documentation

Thank you for helping make AWS security more accessible and robust!
