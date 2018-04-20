import pystache

EXPERIMENT_TEMPLATE_ANDROID = """package ru.koss.lib.tests
    /**
    * THIS CODE WAS AUTOGENERATED
    * YOU CANNOT MODIFY THIS FILE.
    */
    enum class {{experimentName}} : BaseTest {
    {{#variants}}
    {{experimentVariantName}} {
        override fun getExperimentVariantDescription(): String = \"{{experimentVariantDescription}}\"
        override fun getExperimentValue(): String = \"{{experimentVariantConfigValue}}\"
        {{#experimentValues}}
        override fun {{experimentValueName}}(): {{experimentValueType}} = \"{{experimentValue}}\"
        {{/experimentValues}}
    },
    {{/variants}}
    DEF_EXPERIMENT {
    override fun getExperimentVariantDescription(): String = \"default variant\"
    override fun getExperimentValue(): String = \"DEF\"
    };
    override fun getExperimentKey(): String = \"{{experimentName}}\"
    {{#defaultValues}}
    open fun {{experimentValueName}}(): {{experimentValueType}} = \"{{experimentValue}}\"
    {{/defaultValues}}
    };"""

EXPERIMENT_TEMPLATE_IOS = """class {{experimentName}} : Experiment {
    override func name() -> String {
        return \"{{experimentName}}\"
    }

    override func variants() -> Dictionary<String, Variant> {
        return [
        {{#variants}}
        \"{{experimentVariantName}}\" : Variant(name: \"{{experimentVariantName}}\", description: \"{{experimentVariantDescription}}\", values:
        [{{#experimentValues}}
        VariantValue(name: \"{{experimentValueName}}\",value: \"{{experimentValue}}\"),
        {{/experimentValues}}]),
        {{/variants}}
        ]
    }

    override func defaultVariant() -> Variant {
        return Variant(name: "DEF_VARIANT", description: "def variant", values:
        [
        {{#defaultValues}}
        VariantValue(name: \"{{experimentValueName}}\",value: \"{{experimentValue}}\"),
        {{/defaultValues}}
        ])
    }
}"""

def generateExperimentClass( abtestobj ):
    return pystache.render(EXPERIMENT_TEMPLATE_IOS, abtestobj)
