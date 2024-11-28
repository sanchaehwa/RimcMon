# 🏫 대학생을 위한 리크루팅 서비스 , 림크몬 👾
대학생을 위한 프로젝트 / 공모전 등의 매칭 서비스를 제공하는 림크몬 👾 개발 저장소입니다. <br> 
림크몬은 대학생이 자신의 관심사와 전공 등 역량에 맞는 활동에 참여할 수 있도록 돕는 매칭 서비스입니다.<br> 
다양한 활동을 통해 자신의 역량을 성장시키고, 새로운 기회를 발견하는 것을 목표로 합니다.<br>
### 🧑🏻‍💻 Developers 

| [<img src="https://avatars.githubusercontent.com/bum0w0" width="100px;" alt="bum0w0"/>](https://github.com/bum0w0) | [<img src="https://avatars.githubusercontent.com/chanyoung1256" width="100px;" alt="chanyoung1256"/>](https://github.com/Hermes765) | [<img src="https://avatars.githubusercontent.com/sanchaehwa" width="100px;" alt="sanchaehwa"/>](https://github.com/sanchaehwa) | [<img src="https://avatars.githubusercontent.com/krdevdory" width="100px;" alt="krdevdory"/>](https://github.com/krdevdory) |
|:---------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| **김진범**                                                                                                      | **김찬영**                                                                                                       | **양화영**                                                                                                         | **안봉근**                                                                                                       |

###  💭 Message Format
 | Message Type      | Description          | Example               |
|:----------------:|:--------------------:|:---------------------:|
| Issue          | 이슈 작성시,이슈 메시지에 <수정사항> 작성후, 수정사항에 대해 간단히 작성 | `<수정사항> README.md 수정` |
| Commit        | 이슈번호 + [키워드] + 수정사항| `#1 [Docs] README.md 수정`   |
| PullRequest  | 이슈번호 + [키워드] + 수정사항   | `#1 [Docs] README.md 수정`|

### 🔑 Keyword Type
|태그 이름|태그 설명|
|:---:|:---:|
|✨ Feat|새로운 기능 추가|
|🐛 Fix|버그 수정|
|🚑 HOTFIX|치명적 버그 수정|
|📁 Build|빌드 관련 파일 수정|
|🎨 Design|CSS를 포함 UI 디자인 변경|
|📄 Docs|문서(문서 추가, 수정, 삭제)|
|📝Test|테스트(테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없는 경우)|
|♻️ Rename|파일, 폴더명 이름 수정|
|🔥 Remove|파일, 폴더 삭제|

### 🎋 Branch Convention
#### Branch Structure 
- **main**: 배포용 브랜치 (항상 안정적인 상태 유지)
- **develop**: 통합 개발 브랜치 (다음 배포를 준비)
- **feature/**: 기능 개발 및 이슈 해결 브랜치 (작업 단위)
#### Branch Flow
 ```
Main Branch
  ▲
  └── Develop Branch ── 테스트 완료 후 병합 
                              ▲
                              └── Feature Branch ── 작업 완료 후 병합 
                                          └── 새로운 기능 추가

 ```
#### RuleSet
1. Reviewer가(2명 이상) PR을 승인할 시에, PR Merge 가능
2. PR에 새로운 commit 추가 시, 이전의 PR 승인을 무효화하고 재검토
